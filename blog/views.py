from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def home(request):
    # Postモデルから最新の3つを取得
    posts = Post.objects.order_by("-date_posted")[:3]
    return render(request, "home.html", {"posts": posts})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {"posts": posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "post_detail.html", {"post": post})
