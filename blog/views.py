from django.shortcuts import get_object_or_404, redirect, render

from blog.forms import PostForm
from blog.models import Post


def post_list(request):
    posts = Post.objects.all().order_by("-date_posted")
    return render(request, "post_list.html", {"posts": posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "post_detail.html", {"post": post})


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = PostForm()
    return render(request, "post_create.html", {"form": form})
