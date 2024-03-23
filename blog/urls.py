from django.urls import path
from .views import home, post_list, post_detail


urlpatterns = [
    path("", home, name="home"),
    path("posts/", post_list, name="post_list"),
    path("post/<int:post_id>", post_detail, name="post_detail")
]
