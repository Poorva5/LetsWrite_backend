from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    # user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['title','category', 'author', 'body', 'image', 'published_on', 'created_at', 'updated_at', 'status']