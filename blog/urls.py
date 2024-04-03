from django.urls import path

from blog.views import post_create, post_detail, post_list


urlpatterns = [
    path("", post_list, name="post_list"),
    path("post/<int:post_id>", post_detail, name="post_detail"),
    path("post/new/", post_create, name="post_create"),
]
