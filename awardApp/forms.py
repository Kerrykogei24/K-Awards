from django import forms
from .models import Projects,Profile,Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import NewProjectForm,CommentForm,EditProfileForm
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user','project_id']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

