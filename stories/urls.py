from django.contrib import admin
from django.urls import path, include
from rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dj-rest-auth/", include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
     path('rest-auth/password/reset/confirm/<uidb64>/<str:token>', PasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),
    path('api/post/',  include('posts.urls'))
]
