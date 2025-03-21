from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('auth/', views.auth_view, name='auth'),
    path('yandex-auth/', views.yandex_auth, name='yandex_auth'),
    path('oauth_callback/', views.oauth_callback, name='oauth_callback'),
    path('logout/', views.logout_view, name='logout_view'),
]