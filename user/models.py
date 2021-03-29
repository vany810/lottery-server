from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField('头像', upload_to='avatar', null=True, blank=True)
    wechat_avatar = models.URLField('微信头像', blank=True)
    name = models.CharField('名字', max_length=20, blank=True)
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name or self.username
