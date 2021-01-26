from django import forms
from .models import Projects,Profile,Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

