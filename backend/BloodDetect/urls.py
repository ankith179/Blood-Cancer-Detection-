from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Blood Cancer Detection System Running")

urlpatterns = [
    path('', home),
]
