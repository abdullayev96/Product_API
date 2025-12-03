from django.urls import path
from .views import *


urlpatterns = [
    path('category', CategoryAPI.as_view())
]