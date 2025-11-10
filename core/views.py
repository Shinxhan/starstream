from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Movie, MovieList
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .serializers import MovieSerializer, MovieListSerializer, UserSerializer
import re

# Create your views here.
@login_required(login_url='login')
def index(request):
    movies = Movie.objects.all()
    featured_movie = movies.last()

    context = {
        'movies': movies,
        'featured_movie': featured_movie,
    }
    return render(request, 'index.html', context)

@login_required(login_url='login')
def movie(request, pk):
    movie_uuid = pk
    movie_details = Movie.objects.get(uu_id=movie_uuid)

    context = {
        'movie_details': movie_details
    }

    return render(request, 'movie.html', context)

@login_required(login_url='login')
def genre(request, pk):
    movie_genre = pk
    movies = Movie.objects.filter(genre=movie_genre)

    context = {
        'movies': movies,
        'movie_genre': movie_genre,
    }
    return render(request, 'genre.html', context)

@login_required(login_url='login')
def search(request):
    if request.method == 'POST':
        search_term = request.POST['search_term']
        movies = Movie.objects.filter(title__icontains=search_term)

        context = {
            'movies': movies,
            'search_term': search_term,
        }
        return render(request, 'search.html', context)
    else:
        return redirect('/')

@login_required(login_url='login')
def my_list(request):

    movie_list = MovieList.objects.filter(owner_user=request.user)
    user_movie_list = []

    for movie in movie_list:
        user_movie_list.append(movie.movie)

    context = {
        'movies': user_movie_list
    }
    return render(request, 'my_list.html', context)

@login_required(login_url='login')
def add_to_list(request):
    if request.method == 'POST':
        movie_url_id = request.POST.get('movie_id')
        uuid_pattern = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
        match = re.search(uuid_pattern, movie_url_id)
        movie_id = match.group() if match else None

        movie = get_object_or_404(Movie, uu_id=movie_id)
        movie_list, created = MovieList.objects.get_or_create(owner_user=request.user, movie=movie)

        if created:
            response_data = {'status': 'success', 'message': 'Added ✓'}
        else:
            response_data = {'status': 'info', 'message': 'Movie already in list'}

        return JsonResponse(response_data)
    else:
        # return error
        return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password is invalid')
            return redirect('login')
    
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # log user in
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                return redirect('/')
        else:
            messages.info(request, 'Passwords does not match')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

@login_required(login_url='login')
def logout_view(request):
    auth.logout(request)
    return redirect('login')

'''DRF'''
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def genre_movies(request, pk):
    movies = Movie.objects.filter(genre=pk)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def search_movies(request):
    q = request.GET.get('q', '')
    movies = Movie.objects.filter(title__icontains=q)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def my_list_api(request):
    movie_list = MovieList.objects.filter(owner_user=request.user)
    serializer = MovieListSerializer(movie_list, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_list_api(request):
    movie_id = request.data.get('movie_id')
    movie = get_object_or_404(Movie, uu_id=movie_id)
    movie_list, created = MovieList.objects.get_or_create(owner_user=request.user, movie=movie)
    if created:
        return Response({'status': 'success', 'message': 'Added ✓'})
    return Response({'status': 'info', 'message': 'Movie already in list'})

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def signup_api(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)
    user = User.objects.create_user(username=username, email=email, password=password)
    return Response(UserSerializer(user).data)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def user_login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return Response({'message': 'Login successful'})
    return Response({'error': 'Invalid credentials'}, status=401)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def user_logout_api(request):
    logout(request)
    return Response({'message': 'Logged out'})
