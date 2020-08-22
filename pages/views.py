from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def index(request):
    print(os.getcwd()+"/templates/pages/index.html");
    return render(request, "pages/index.html")

