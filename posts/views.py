from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from posts import models
from . import serializers

class PostList(ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer