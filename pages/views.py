from django.shortcuts import render


def home_view(requset):
    return render(requset, 'index.html')
