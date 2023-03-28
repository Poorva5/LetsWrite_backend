from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    # user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    created_at = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    author = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    class Meta:
        model = Post
        fields = [
            'id','title', 'first_name', 'email', 'author', 'body', 'image', 'published_on', 'created_at', 'updated_at', 'status']

    @staticmethod
    def get_created_at(instance):
        return instance.created_at.strftime("%d %b")

    @staticmethod
    def get_first_name(instance):
        print(instance.author.first_name, 'first name')
        return instance.author.first_name

    
    @staticmethod
    def get_email(instance):
        print(instance.author.email, 'email')
        return instance.author.email