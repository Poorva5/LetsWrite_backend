from .models import Post
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import PostSerializer
from rest_framework.views import APIView

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdate(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CreatePost(APIView):

    def post(self, request):
        try:
            post_serializer = PostSerializer(data=request.data)
            post_serializer.is_valid(raise_exception=True)
            post_instance = post_serializer.save(author=request.user)

            return Response(
                PostSerializer(post_instance).data, status=status.HTTP_200_OK
            )
        except Exception as e:
            print(e)
            return Response(
                post_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )