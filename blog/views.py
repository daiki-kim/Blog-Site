from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from .forms import PostForm, UserRegisterForm


# ホームページ
def home(request):
    posts = Post.objects.order_by("-date_posted")[:3]
    return render(request, "home.html", {"posts": posts})


# ブログ一覧ページ
def post_list(request):
    posts = Post.objects.all().order_by("-date_posted")
    return render(request, 'post_list.html', {"posts": posts})


# ブログ記事の詳細ページ
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "post_detail.html", {"post": post})


# ユーザー登録ページ
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


# ユーザープロフィールページ（ログイン時のみ）
@login_required
def profile(request):
    user_posts = Post.objects.filter(author=request.user).order_by("-date_posted")
    return render(request, "profile.html", {"user_posts": user_posts})


# ブログ投稿ページ（ログイン時のみ）
@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect("post_list")
    else:
        form = PostForm()
    return render(request, "post_create.html", {"form": form})
