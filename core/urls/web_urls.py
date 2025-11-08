from django.urls import path
from core.viewss import web_views

urlpatterns = [
    path("register/", web_views.register_page, name="register_page"),
    path("login/", web_views.login_page, name="login_page"),
    path("profile/", web_views.profile_page, name="profile_page"),
    path("edit-profile/", web_views.edit_profile, name="edit_profile"),  
]
