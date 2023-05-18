from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from core.models import User

def index(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("explore"))
        else:
            return render(request, "login.html", {
                "validationError": "Invalid email or password"
            })

    

def register(request):
    if request.method == "POST" :
        try:
            email = request.POST["email"]
            password = request.POST["password"]        
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            user = User.objects.create_user( email=email, password=password,first_name=first_name,last_name=last_name)
            user.save()
            print (user)
            logout(request)
            return HttpResponseRedirect(reverse("home"))
        except Exception as e:
            print (str(e) )

            return render(request , "register.html" , {
                "validationError":str(e) 
            })
    return render(request , "register.html")




def explore(request):
    return render(request, 'explore.html')

