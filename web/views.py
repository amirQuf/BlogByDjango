from django.shortcuts import render

from rest_framework import generics  
from .serializers import (PostSerializer,CategorySerializer ,FollwerSerializer
, savepostSerializer , ProfileSerializer , UserSerializer) 
from  users.models import Profile ,Follower
from .models import Post ,Category ,SavePost , Comment
from django.contrib.auth.models import User
# from rest_framework.viewsets import  ViewSet


# class PostViewSet(ViewSet):
#     queryset=Profile.objects.all()
#     serializer_class = ProfileSerializer


# class CatgoryViewSet(ViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class Profileview(generics.RetrieveUpdateDestroyAPIView):
    queryset=Profile.objects.all()
    serializer_class = ProfileSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostList(generics.ListAPIView):
    queryset = Post.objects.filter(status='P')
    serializer_class = PostSerializer

class PosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.filter(status='P')
    serializer_class = PostSerializer

class CatgoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class savedPostList(generics.ListCreateAPIView):
    queryset = SavePost.objects.all()
    serializer_class = savepostSerializer

class FollowerList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollwerSerializer