from django.shortcuts import render


def login(request):
    context = {'title': 'Geekshop - �����������'}
    return render(request, 'users/login.html', context)


def register(request):
    context = {'title': 'Geekshop - �����������'}
    return render(request, 'users/register.html', context)
