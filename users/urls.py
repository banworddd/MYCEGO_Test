from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.auth_view, name='auth'),
    path('yandex-auth/', views.yandex_auth, name='yandex_auth'),
    path('oauth_callback/', views.oauth_callback, name='oauth_callback'),
]