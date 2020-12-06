from django.urls import path
from .views import todo

urlpatterns = [
    path('test/', todo)
]
