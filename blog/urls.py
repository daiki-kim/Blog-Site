from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, post_create, post_detail, post_list, profile, register


urlpatterns = [
    path("", home, name="home"),
    path("posts/", post_list, name="post_list"),
    path("post/<int:post_id>", post_detail, name="post_detail"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("post/new/", post_create, name="post_create")
]
