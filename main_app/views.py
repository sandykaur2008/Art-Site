from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Piece, Profile
from .forms import LoginForm, RegisterForm, ContactForm, UserForm, EditProfileForm
from django.contrib.auth import authenticate, login, logout
# pylint: disable=E1101
# Create your views here.

def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      u = form.cleaned_data['username']
      p = form.cleaned_data['password']
      user = authenticate(username = u, password = p)
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponseRedirect('/')
        else:
          print('The account has been disabled')
      else:
        print('The username and password were incorrect.')
  else:
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
  logout(request)
  return HttpResponseRedirect('/')

def register(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      login(request, user)
      return HttpResponseRedirect('/')
  else:
    form = RegisterForm()
  return render(request, 'register.html', {'form': form})

def index(request):
  users = User.objects.all()
  return render(request, 'index.html', {'users': users})

def about(request):
  return render(request, 'about.html')

def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      return HttpResponseRedirect('/')
  else:
    form = ContactForm()
  return render(request, 'contact.html', {'form': form})

def profile(request, username):
  user = User.objects.get(username=username)
  pieces = Piece.objects.filter(user=user)
  profile = Profile.objects.get(user=user)
  return render(request, 'profile.html',
                {'user': user,
                'pieces': pieces,
                'profile': profile})

@login_required
def edit_profile(request):
  if request.method == 'POST':
    user_form = UserForm(request.POST, instance=request.user)
  return render(request, 'edit_profile.html')

# def detail(request, piece_id):
#   piece = Piece.objects.get(pk=piece_id)
#   return render(request, 'detail.html', {'piece': piece})

# def reset_password(request):
#   return render(request, 'reset_password.html')

# def reset_password_request(request):
#   return render(request, 'reset_password_request.html')

