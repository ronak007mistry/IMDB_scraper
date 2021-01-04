from django.db.models import Q
from django.shortcuts import render
from rest_framework import permissions, response
from scraper.models import Movie
from .serializers import MovieSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import MyPagination



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


class MovieListApiView(ListAPIView):
    # queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'ratings', 'release_date', 'duration', 'description']
    pagination_class = MyPagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Movie.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(ratings__icontains=query)|
                Q(release_date__icontains=query)|
                Q(duration__icontains=query)|
                Q(description__icontains=query)

            )
        return queryset_list
    


class MovieDetailApiView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]


