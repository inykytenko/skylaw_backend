
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def my_view(request):
    if request.method == 'get':
        return HttpResponse('result')
    

class MyView(View):
    def get(self, request):
        return HttpResponse('result')
    
    def post(self, request):
        return HttpResponse('result')
    