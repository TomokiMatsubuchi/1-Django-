from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blogapp.models import Post
from django.core.exceptions import PermissionDenied
# Create your views here.

class PostList(ListView):
  model = Post
  template_name = "blogapp/index.html"
  context_object_name = "posts"

class PostDetail(DetailView):
  model = Post
  context_object_name = "post"
  template_name = "blogapp/show.html"

  def get_object(self):
    post = super().get_object()
    if post.is_published or self.request.user.is_authenticated:
      return post
    else:
      raise PermissionDenied

