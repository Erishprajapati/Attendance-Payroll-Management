from django.urls import path, include
from attendance.api.v1 import *
urlpatterns = [
    path("api/v1/", include("attendance.api.v1.urls"))
]
