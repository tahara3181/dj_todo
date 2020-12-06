from django.urls import path
from .views import todo, signupview

urlpatterns = [
    path('signup/', signupview, name='signup'),
    path('test/', todo)
]
