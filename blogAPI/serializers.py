from rest_framework import serializers

from blogAPI.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'body', 'author', 'created_at']