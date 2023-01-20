from django.urls import path

from .views import RegisterView
from .views import *
urlpatterns = [
    path('register/', RegisterView.as_view()),
]