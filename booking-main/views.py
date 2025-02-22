from django.shortcuts import render , redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib import messages


def register(request):
    if request.method =="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("room-list")
        else:
            from = CustomUserCreationForm()
            messages.error(request,"Leck Eier")
            context = {
                "form":form, 
            }
            return render(request,
                          'auth_syste,/register.html',
                          context)