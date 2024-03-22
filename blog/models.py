from django.db import models
# djangoの組み込みユーザー認証システム
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    # データがpostされると自動的にその日時が入る
    date_posted = models.DateTimeField(auto_now_add=True)
    # Userモデルに関連付けている, 特定のユーザが削除されるとそのユーザに紐づくPostモデルも削除される
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    