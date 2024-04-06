from django.shortcuts import render, redirect
from .forms import MentorForm
from django.contrib import messages
from . models import Mentor

# Create your views here.

def  home(request):
    mentors = Mentor.objects.all()
    return render (request, 'index.html', {'mentors': mentors})


def register(request):
    if request.method == "POST":
        form = MentorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mentor registered successfully')
            return redirect('home')
    else:
        form = MentorForm()
        return render(request, "register.html", {"form": form})
