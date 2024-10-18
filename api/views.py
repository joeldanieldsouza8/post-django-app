from typing import Never, override

from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .serializers import PostSerializer
from rest_framework import viewsets, generics
from django.db.models import QuerySet

from .models import Post


class CreatePostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()  # Queries all the posts in the database
    serializer_class = PostSerializer


class GetPostView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'  # This matches the custom parameter in the URL


class GetAllPostsView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # @override
    # def get_queryset(self) -> QuerySet[Post]:
    #     return Post.objects.order_by('-id')[:3]


class UpdatePostView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DeletePostView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer