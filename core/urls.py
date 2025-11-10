from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('movies', views.MovieViewSet, basename='movie')

urlpatterns = [
    # HTML Pages
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('movie/<str:pk>/', views.movie, name='movie'),
    path('genre/<str:pk>/', views.genre, name='genre'),
    path('my-list/', views.my_list, name='my-list'),
    path('add-to-list/', views.add_to_list, name='add-to-list'),
    path('search', views.search, name='search'),

    # API Routes
    path('api/', include(router.urls)),
    path('api/genres/<str:pk>/', views.genre_movies, name='api-genre'),
    path('api/search/', views.search_movies, name='api-search'),
    path('api/my-list/', views.my_list_api, name='api-my-list'),
    path('api/add-to-list/', views.add_to_list_api, name='api-add-to-list'),
    path('api/signup/', views.signup_api, name='api-signup'),
    path('api/login/', views.user_login_api, name='api-login'),
    path('api/logout/', views.user_logout_api, name='api-logout'),
]
