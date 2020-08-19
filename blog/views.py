from django.shortcuts import render
from .models import Post


# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts':posts})


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    posts = Post.objects.all()[:3]
    return render(request, 'blog/post.html', {'post': post, "posts":posts})