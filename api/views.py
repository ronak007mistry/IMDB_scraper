from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions, response
from scraper.models import Movie
from .serializers import MovieSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination, CursorPagination
from django.core.paginator import Paginator



@api_view(['GET'])
def apiOverview(request):
    api_urls = {
		'Movies List':'/movies/',
		'Movies Detail View':'/movies/<int:pk>/',
		'Login':'/login/',
		'Register':'/registration/',
		'Logout':'/logout/',
		}

    return Response(api_urls)


class MyPagination(CursorPagination):
    page_size = 10




class MovieList(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    pagination_class = MyPagination

    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = MovieSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetail(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     movie = self.get_object(pk)
    #     serializer = MovieSerializer(movie, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     movie = self.get_object(pk)
    #     movie.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)