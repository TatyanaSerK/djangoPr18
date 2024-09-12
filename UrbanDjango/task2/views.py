from django.shortcuts import render

# Create your views here.

def index1(request):
    return render(request, 'class_template.html')

def index2(request):
    return render(request, 'func_template.html')