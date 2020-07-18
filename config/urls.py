from django.contrib import admin
from django.urls import path
from authentication.views import registration_view, example_view # 추가
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/', registration_view, name='register_user'),
    path('api/auth/login/', obtain_auth_token, name='login'),
    path('api/test/', example_view, name='example_view'), # 추가

]
