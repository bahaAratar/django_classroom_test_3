from django.db import models
from test1.models import Post

class Commets(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        db_table = 'Comment'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
