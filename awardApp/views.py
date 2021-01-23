from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile,Projects,Comments,Ratings
from django.contrib.auth.models import User


# Create your views here.

def index(request):

    all_projects = Projects.all_projects()
    return render(request,'index.html',{'all_projects':all_projects})


