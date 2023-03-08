from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    author = models.CharField()
    author = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']