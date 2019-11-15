from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response #render와 redirect 대신
from .models import Movie
from .serializers import MovieSerializer
# Create your views here.

@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PATCH', 'DELETE'])
def one_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    # GET 요청 들어오면
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    # 수정 요청 들어오면
    elif request.method == 'PATCH':
        serializer = MovieSerializer(data=request.data, instance=movie)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Movie Edited!'})

    # 삭제 요청 들어오면
    else:
        movie.delete()
        return Response({'message': 'Movie Deleted!'})


@api_view(['POST'])
def create_movie(request):
    # movie = Movie() 객체 생성 필요없음
    serializer = MovieSerializer(data=request.data)
    # 유효성 검사 꼭 해줘야함
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
