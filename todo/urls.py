from django.urls import path
from .views import todo, signupview, loginview

urlpatterns = [
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('test/', todo)
]
