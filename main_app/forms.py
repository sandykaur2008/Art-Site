from django import forms 
from .models import Piece, Profile, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PieceForm(forms.ModelForm):
  class Meta:
    model = Piece
    fields = ['name', 'img_url']

class ContactForm(forms.Form):
  text = forms.CharField(widget=forms.Textarea, label='Questions/Comments', max_length=500)
  email = forms.EmailField(label='Email', max_length=50)
  name = forms.CharField(label='Name', max_length=20)

#will combine the next two forms in appropriate templates 
class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email']

class EditProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['bio', 'img_url']

class RegisterForm(UserCreationForm):
  first_name = forms.CharField(label='First Name', max_length=30)
  last_name = forms.CharField(label='Last Name', max_length=30)
  email = forms.EmailField(label='Email', max_length=50)

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
  
class LoginForm(forms.Form):
  username = forms.CharField(label='Username', max_length=64)
  password = forms.CharField(widget=forms.PasswordInput())

class PostForm(forms.Form):
  class Meta:
    model = Post
    fields = ['body']