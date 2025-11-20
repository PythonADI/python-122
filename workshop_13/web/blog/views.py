from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 1
    ordering = ["-created_at"]
    template_name = "post_list.html"
    context_object_name = "posts"
