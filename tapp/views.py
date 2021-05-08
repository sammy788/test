from django.shortcuts import render
import os
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == "POST":
        try: 
            os.system("bash cpp/selll.sh")
            messages.success(request, "SUCCESS!")
        except:
            messages.error(request,"ERROR :(")
    return render(request,"index.html")
