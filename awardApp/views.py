from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile,Projects,Comments,Ratings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):

    all_projects = Projects.all_projects()
    return render(request,'index.html',{'all_projects':all_projects})

def profile(request):

    all_projects = Projects.objects.filter(user = request.user)
    return render(request,'profile.html',{'all_projects':all_projects})

def new_project(request):
    if request.method=='POST':
        form = NewProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()

            return redirect('home')

    else:
        form = NewProjectForm()
    return render(request,'new_project.html',{'form':form})

def search_results(request):

    if 'project' in request.GET and request.GET['project']:
        search_term = request.GET.get('project')
        searched_projects = Projects.search_project(search_term)
        message = f'{search_term}'

        return render(request,'search.html',{'message':message,'project':searched_projects})

    else:
        message = 'You have not entered anything to search'
        return render(request,'search.html',{'message':message})

def comment(request,id):
    id = id
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.user = request.user
            project = Projects.objects.get(id = id)
            comment.project_id = project
            comment.save()
            return redirect('home')

        else:
            project_id = id
            messages.info(request,'MAke sure you fill all the fields')
            return redirect('comment',id = project_id)

    else:
        id = id
        form = CommentForm()
        return render(request,'comment.html',{'form':form,'id':id})

def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')

    else:
        form = EditProfileForm(request.POST,request.FILES)
    return render(request,'update_profile.html',{'form':form})

    