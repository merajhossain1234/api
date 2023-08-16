from django.urls import path
from .import views
urlpatterns = [
    path("signup/", views.SignupAPIView.as_view(), name="user-signup"),
    path("login/", views.LoginAPIView.as_view(), name="user-login"),
    path("studentpost/",views.StudentAPIViewforpost.as_view(), name="studentpost"),
    path("studentget/",views.StudentAPIView.as_view(), name="studentget"),
    path("logout/",views.Logout.as_view(), name="user-logout"),
    
]