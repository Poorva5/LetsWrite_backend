from django.urls import path, include
from .views import PostList, CreatePost, PostDetail, PostUpdate, PostDelete


urlpatterns = [ 
    path('list/', PostList.as_view()),
    path('create/', CreatePost.as_view()),
    path('detail/<int:pk>/', PostDetail.as_view()),
    path('update/<int:pk>/', PostUpdate.as_view()),
    path('delete/<int:pk>/', PostDelete.as_view()),
]