from django.urls import path, include
from .views  import UserDetail

urlpatterns = [ 
    path('detail/', UserDetail.as_view())
]