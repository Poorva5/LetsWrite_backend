from django.urls import path, include
from .views  import UserDetail, MyProfile

urlpatterns = [ 
    path('detail/', UserDetail.as_view()),
    path('<int:pk>/profile/', MyProfile.as_view())
]