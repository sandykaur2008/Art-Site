from django import forms 
from .models import Piece, Profile, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PieceForm(forms.ModelForm):
  class Meta:
    model = Piece
    fields = ['name', 'image']

class EditPieceForm(forms.ModelForm):
  image = forms.ImageField(label='Image', required=False, widget=forms.FileInput)
  delete_piece = forms.BooleanField(label='Delete', required=False)
  class Meta:
    model = Piece
    fields = ['name', 'image', 'delete_piece']

class ContactForm(forms.Form):
  text = forms.CharField(widget=forms.Textarea, label='Questions/Comments', max_length=500)
  email = forms.EmailField(label='Email', max_length=50)
  name = forms.CharField(label='Name', max_length=20)

#will combine the next two forms in appropriate templates (profile editing)
class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email']

class EditProfileForm(forms.ModelForm):
  image = forms.ImageField(label='Image', required=False, widget=forms.FileInput)
  class Meta:
    model = Profile
    fields = ['image', 'bio']

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

class PostForm(forms.ModelForm):
  body = forms.CharField(widget=forms.Textarea, label='Post Here')
  class Meta:
    model = Post
    fields = ['body']