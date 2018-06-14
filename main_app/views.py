from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Piece, Profile
from django.contrib.auth import authenticate, login, logout
# pylint: disable=E1101
# Create your views here.

def index(request):
  users = User.objects.all()
  return render(request, 'index.html', {'users': users})

def profile(request, username):
  user = User.objects.get(username=username)
  pieces = Piece.objects.filter(user=user)
  profile = Profile.objects.get(user=user)
  return render(request, 'profile.html',
                {'username': username,
                'pieces': pieces,
                'profile': profile})

def contact(request):
  return render(request, 'contact.html')

def about(request):
  return render(request, 'about.html')

def detail(request, piece_id):
  piece = Piece.objects.get(pk=piece_id)
  return render(request, 'detail.html', {'piece': piece})

def edit_profile(request):
  return render(request, 'edit_profile.html')

def login_view(request):
  return render(request, 'login.html')

def logout_view(request):
  logout(request)
  return redirect('index.html')

def register(request):
  return render(request, 'register.html')

def reset_password(request):
  return render(request, 'reset_password.html')

def reset_password_request(request):
  return render(request, 'reset_password_request.html')

