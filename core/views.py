from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout as auth_logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from core.models import User ,Job





login_required   =   login_required ( login_url = "home" )






def index(request):
    query = request.GET.get("next") 
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("explore"))
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if query:
                return HttpResponseRedirect(reverse(query))
            if user.is_company:
                return HttpResponseRedirect(reverse("dashboard"))
            return HttpResponseRedirect(reverse("explore"))
        else:
            return render(request, "login.html", {
                "validationError": "Invalid email or password"
            })

    
@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("home"))



def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("explore"))
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



@login_required
def explore(request):
    jobs = Job.objects.order_by("-date")[0:9]
    return render(request, 'explore.html',{
        jobs:jobs
    })



def company_signup(request):
    if request.user.is_authenticated and request.user.is_company:
        return HttpResponseRedirect(reverse("explore"))
    if request.method == "POST" :
        try:
            email = request.POST["email"]
            password = request.POST["password"]   
            user = User.objects.create_user( email=email, password= password,is_company=True)
            print(user)
            user.save()
            print (user)
            return HttpResponseRedirect(reverse("dashboard"))
        except Exception as e:
            return render(request, 'company-signUp/companySignUp.html'  , {
                "validationError":str(e) 
            } )

    return render(request, 'company-signUp/companySignUp.html')


@login_required
def dashboard(request):
    if request.user.is_company:
        return HttpResponseRedirect(reverse("explore"))
    if request.method == "POST" :
        try:
            email = request.POST["email"]
            password = request.POST["password"]   
            user = User.objects.create_user( email=email, password= password,is_company=True)
            print(user)
            user.save()
            print (user)
            return render(request, 'company-signUp/companySignUp.html')
        except Exception as e:
            return render(request, 'company-signUp/companySignUp.html'  , {
                "validationError":str(e) 
            } )
    return render(request,  'company-signUp/dashboard.html')

