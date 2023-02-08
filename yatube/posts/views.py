from django.shortcuts import render, get_object_or_404
from .models import Post, Group

POST_PER_PAGE: int = 10


def index(request):
    posts = Post.objects.all()[:POSTS_PER_PAGE]
    template = 'posts/index.html'
    context = {
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_PER_PAGE]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, template, context)
