from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Movie, MovieList

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    class Meta:
        model = MovieList
        fields = ['id', 'movie']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
