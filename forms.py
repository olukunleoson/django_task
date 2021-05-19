from django.db.models import fields
from bloghome.models import Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

class Registration_form(UserCreationForm):
    user = forms.CharField(max_length=20, help_text='Username')
    first_name = forms.CharField(max_length=20, help_text='First Name')
    last_name = forms.CharField(max_length=20, help_text='Last Name')
    password = forms.PasswordInput
    email = forms.EmailField

    class Meta(UserCreationForm.Meta):
        fields = ('first_name', 'last_name', 'password1', 'email',)

class CommentForm(forms.ModelForm):
    email = forms.EmailField

    class Meta(forms.ModelForm):
        model = Comment
        fields = ('text',)