from .views import LoginAPI, UserRegistrationView, VerifyEmail
from django.urls import path
urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='signup'),
    path("verify/<path:token>/",VerifyEmail.as_view())
]
