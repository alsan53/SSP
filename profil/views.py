from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def berita(request):
    return render(request,'berita.html')

def about(request):
    return render(request,'about.html')

def price(request):
    return render(request,'price.html')