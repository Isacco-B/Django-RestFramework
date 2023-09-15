from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from .models import Post, Comment
from .serializer import PostSerializer, OwnerSerializer, CommentSerializer
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT,
)

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .permissions import IsOwnerPermission
from django.contrib.auth import get_user_model


User = get_user_model()


class PostView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwatgs):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)

        # if serializer.is_valid():
        return Response(serializer.data)

    def post(self, request, *args, **kwatgs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwatgs):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwatgs):
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response(status=HTTP_400_BAD_REQUEST)


@csrf_exempt
def post_list(request):
    if request.method == "GET":
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        data = JSONParser.parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser.parse(post)
        serializer = PostSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error, status=400)

    elif request.method == "DELETE":
        post.delete()
        return HttpResponse(status=204)


@api_view(["GET", "POST"])
def posts_list(request):
    if request.method == "GET":
        pass

    if request.method == "POST":
        pass


class PostMixingListView(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwatgs):
        return self.list(request, *args, **kwatgs)

    def post(self, request, *args, **kwatgs):
        return self.create(request, *args, **kwatgs)


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsOwnerPermission,)


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsOwnerPermission,)


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = (AllowAny,)


class OwnerDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = OwnerSerializer


class CommentDetailView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        AllowAny,
    )
