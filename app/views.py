from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def bill(request):
    return render(request, 'bill.html')


