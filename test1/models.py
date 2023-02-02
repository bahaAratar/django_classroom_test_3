from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'Post'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
