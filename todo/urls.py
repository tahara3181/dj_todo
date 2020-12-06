from django.urls import path
from .views import signupview, loginview, TodoList

urlpatterns = [
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('', TodoList.as_view(), name='list'),
]
