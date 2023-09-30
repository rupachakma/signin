from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth


def homep(request):
    return render(request,"home.html")

def loginp(request):
    if request.method=="POST":
        nm=request.POST.get("username")
        pa=request.POST.get("pas")
        u=auth.authenticate(username=nm,password=pa)
        if u is not None:
            return redirect("loginp")
        else:
            return redirect("homep")
        
    return render(request,"login.html")
   
def signupp(request):
    if request.method=="POST":
        un=request.POST.get("username")
        f=request.POST.get("fn")
        l=request.POST.get("ln")
        em=request.POST.get("email")
        pas1=request.POST.get("password1")
        pas2=request.POST.get("password2")
        if pas1==pas2:
            u=User.objects.create_user(username=un,password=pas1,first_name=f,last_name=l,email=em)
            u.save()
            return redirect("loginp")

        else:
            return redirect("signupp")
    return render(request,"signup.html")

   