from django.shortcuts import render
import os
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == "POST":
        try: 
            os.system("./fuck.sh")
            messages.success(request, "CONGRATS YOU GOT WIDE VIEW BITCH!")
        except:
            messages.error(request,"CPP: I'M NOT GONNA RUN, FUCK OFF!")
    return render(request,"index.html")
