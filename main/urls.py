from django.urls import path
from .views import PostView
from .views import PostDetailView
urlpatterns = [
    path('', PostView.as_view()),
    path('<int:pk>', PostDetailView.as_view())
]