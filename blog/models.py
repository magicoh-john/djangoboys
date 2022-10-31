from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # 게시 일자에 현재 날짜를 대입해주는 함수
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # 객체 주소 대신 글제목을 반환해주는 toString()함수
    def __str__(self):
        return self.title
