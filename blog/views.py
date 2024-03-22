from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    # Postモデルから最新の3つを取得
    posts = Post.objects.order_by("-date_posted")[:3]
    return render(request, "blog/home.html", {"posts": posts})
