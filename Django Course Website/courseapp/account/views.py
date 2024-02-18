from django.shortcuts import render,redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User




##########   LOGIN   ###########

def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:
        return render(request, "account/login.html", {"error":"Icazeniz yoxdur."})
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            nextUrl = request.GET.get("next", None)
            if nextUrl is None:
                return redirect("index")
            else:
                return redirect(nextUrl)
        else:
            return render(request, "account/login.html", {"error":"Username ve ya Password sefdi."})
    else:
        return render(request, "account/login.html")


########    REGISTER  ##########


def user_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password != repassword:
            return render(request, "account/register.html", 
            {
                "error":"Parol tekrari sefdi.",
                "username": username,
                "email": email
            })
        if User.objects.filter(username=username).exists():
            return render(request, "account/register.html", 
            {
                "error":"Username istifade edilir.",
                "username": username,
                "email": email
            })
          
        if User.objects.filter(email=email).exists():
            return render(request, "account/register.html", 
            {
                "error":"Email istifade edilir.",
                "username": username,
                "email": email
            })
              
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect("user_login")
        
    else:
         return render(request, "account/register.html")
   





#########    LOGOUT    ###########

def user_logout(request):
    logout(request)
    return redirect("index")
