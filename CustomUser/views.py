from django.shortcuts import render,HttpResponse


# Test view will be deleted in future
def home(request):
    return HttpResponse('<h1>Hello</h1>')