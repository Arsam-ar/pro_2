from django.shortcuts import render,redirect
from django.views.generic import CreateView,DetailView
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from .forms import RegisterUserForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User




class  ProfileDetailView(LRM,DetailView):
    model = User
    template_name = "acconut/profile.html"
    context_object_name="user"





def login_user(request):
    if request.method== "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None :
            login(request, user)
            return redirect("post:postlist")
        else:
            messages.success(request, ("try again ..."))
            return redirect("acconut:login")
    else:
        return render(request,'acconut/authentication/login.html',{} )






def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,("reqistration successful"))
            return redirect("post:postlist")
    else:
        form = RegisterUserForm()

    return render(request,"acconut/authentication/user_register.html",{"form":form})