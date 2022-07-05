from django.urls import path
from accounts.views.RegisterAPIView import RegisterAPIView
from knox import views as knox_views
from accounts.views.LoginAPI import LoginAPI

urlpatterns = [
    path('api/register/', RegisterAPIView.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logout-all/', knox_views.LogoutAllView.as_view(), name='logout-all'),
]