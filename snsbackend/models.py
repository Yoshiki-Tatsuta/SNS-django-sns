from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os


class SnsPost(models.Model):
    """"投稿内容登録するのに使用"""
    content = models.TextField()
    image = models.ImageField(upload_to="snspost_images", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"SnsPost {self.id} - {self.content}"
    
    @property
    def username(self):
        return self.user.username
    
    def delete(self, *args, **kwargs):
        # 画像の削除処理
        if self.image:
            try:
                os.remove(os.path.join(settings.MEDIA_ROOT, str(self.image)))
            except FileNotFoundError:
                pass  # 画像ファイルが存在しない場合は無視する
        
        # 元のモデルの削除処理を実行
        super().delete(*args, **kwargs)


class UserProfile(models.Model):
    """ユーザの詳細情報を登録するのに使用"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

