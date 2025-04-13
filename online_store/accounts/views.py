from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def signup_view(request:HttpRequest):
    if request.method == "POST":

        try:
            new_user = User.objects.create_user(username=request.POST["username"],password=request.POST["password"],email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"])
            new_user.save()
            messages.success(request, "Registered User Successfuly", "alert-success")
            return redirect("accounts:signin_view")
        except Exception as e:
            print(e)

    return render(request,"accounts/signup.html",{})


def signin_view(request:HttpRequest):

    if request.method == "POST":

        #checking user credentials
        new_user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        print(new_user)
        if new_user:
            #login the user
            login(request, new_user)
            messages.success(request, "Logged in successfully", "alert-success")
            return redirect(request.GET.get("next", "/"))
        else:
            messages.error(request, "Please try again. You credentials are wrong", "alert-danger")



    return render(request, "accounts/signin.html")


def logout_view(request: HttpRequest):

    logout(request)
    messages.success(request, "logged out successfully", "alert-warning")

    return redirect(request.GET.get("next", "/"))