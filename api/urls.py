from django.urls import path, include
from api import views
from rest_framework import urls


app_name = 'api'

urlpatterns = [
    path('movies/', views.MovieListApiView.as_view(), name='allmovies'),
    path('movies/<int:pk>/', views.MovieDetailApiView.as_view(), name='movie'),
    path('', views.apiOverview),
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),

]

