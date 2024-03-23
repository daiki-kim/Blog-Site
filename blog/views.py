from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import UserRegisterForm


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


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}! You can now log in.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "profile.html")