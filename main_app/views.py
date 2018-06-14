from django.shortcuts import render
from .models import Piece 

# Create your views here.
def index(request):
  return render(request, 'index.html')

def profile(request, username):
  user = User.objects.get(username=username)
  pieces = Piece.objects.filter(user=user)
  return render(request, 'profile.html',
                {'username': username,
                'pieces': pieces})

def contact(request):
  return render(request, 'contact.html')

def about(request):
  return render(request, 'about.html')

def detail(request, piece_id):
  piece = Piece.objects.get(id=piece_id)
  return render(request, 'detail.html', {'piece': piece})

def edit_profile(request):
  return render(request, 'edit_profile.html')

def login(request):
  return render(request, 'login.html')

def register(request):
  return render(request, 'register.html')

def reset_password(request):
  return render(request, 'reset_password.html')

