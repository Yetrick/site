from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def blog(request):
    return render(request,'base/blog.html')

def photo(request):
    return render(request,'base/photo.html')

def news(request):
    return render(request, 'base/news.html')