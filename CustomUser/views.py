from django.shortcuts import render,HttpResponse
from django.views import View
from .models import CustomUser
# Test view will be deleted in future
class CustomUserView(View):
    def get(self, request):
        a = CustomUser()
        a.get_user_by_id()
        return HttpResponse("<h1>NEW USER</h1>")