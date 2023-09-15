from django.shortcuts import render
from .models import Post, Author
from .serializers import PostSerializer, PostCreateSerializer
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


def home(request):
    return render(request, "index.html")


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)


@method_decorator(csrf_exempt, name='dispatch')
class PostCreateView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
