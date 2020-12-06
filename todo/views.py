from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import TodoModel
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


class TodoList(ListView):
    template_name = 'index.html'
    model = TodoModel


class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel


def signupview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            user = User.objects.create_user(username_data, '', password_data)
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています'})
    else:
        return render(request, 'signup.html', {})
    return render(request, 'signup.html', {})


def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data,
                            password=password_data)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')


class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'auther', 'priority',
              'progress', 'duedate', 'complete')
    success_url = reverse_lazy('list')


class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')


class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'auther', 'priority',
              'progress', 'duedate', 'complete')
    success_url = reverse_lazy('list')


def logoutview(request):
    logout(request)
    return redirect('login')
