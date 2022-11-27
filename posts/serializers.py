from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    # user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    created_at = serializers.SerializerMethodField()

    author = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    class Meta:
        model = Post
        fields = [
            'id','title', 'author', 'body', 'image', 'published_on', 'created_at', 'updated_at', 'status']

    @staticmethod
    def get_created_at(instance):
        return instance.created_at.strftime("%d %b")