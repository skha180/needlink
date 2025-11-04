from django.urls import path
from core import views

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('profile/', views.UserProfileAPIView.as_view(), name='user_profile'),
]
