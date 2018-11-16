from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Piece, Profile, Post
from .forms import LoginForm, RegisterForm, ContactForm, UserForm, EditProfileForm, PieceForm, PostForm, EditPieceForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import transaction 
from django.core.mail import send_mail 
from django.urls import reverse 
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
          return HttpResponseRedirect(reverse('index'))
        else:
          messages.error(request, 'The account has been disabled')
          return HttpResponseRedirect(reverse('login'))
      else:
        messages.error(request, 'The username and password were incorrect')
        return HttpResponseRedirect(reverse('login'))
  else:
    form = LoginForm()
    return render(request, 'login.html', {'form': form, 'title': 'Login'})

def logout_view(request):
  logout(request)
  return HttpResponseRedirect(reverse('index'))

def register(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      login(request, user)
      return HttpResponseRedirect(reverse('index'))
  else:
    form = RegisterForm()
  return render(request, 'register.html', {'form': form, 'title': 'Register'})

def index(request):
  users = User.objects.all()
  profiles = Profile.objects.all()
  return render(request, 'index.html', {'users': users, 'profiles': profiles, 'title': 'Home'})

def about(request):
  return render(request, 'about.html', {'title': 'About'})

def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      send_mail('Feedback from ArtSite', """
      From: {} <{}>
      {}
      """.format(form.cleaned_data.get('name'), form.cleaned_data.get('email'), form.cleaned_data.get('text')),
      'test69523.2@gmail.com', ['sandykaur2008@gmail.com'])
      messages.success(request, 'Thank you for your feedback!')
      return HttpResponseRedirect(reverse('index'))
  else:
    form = ContactForm()
  return render(request, 'contact.html', {'form': form, 'title': 'Contact'})

def profile(request, username):
  user = User.objects.get(username=username)
  pieces = Piece.objects.filter(user=user)
  profile = Profile.objects.get(user=user)
  form = PieceForm()
  return render(request, 'profile.html',
                {'user': user,
                'pieces': pieces,
                'profile': profile, 'form': form, 'title': user.username
                })

@login_required
@transaction.atomic 
def edit_profile(request):
  user = request.user
  profile = Profile.objects.get(user=user)
  if request.method == 'POST':
    user_form = UserForm(request.POST, instance=request.user)
    profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save(commit = True)
      messages.success(request, 'Your profile was successfully updated!')
      return HttpResponseRedirect(reverse('edit_profile'))
    else:
      messages.error(request, 'Please make sure you entered changes correctly')
  else:
    user_form = UserForm(instance=request.user)
    profile_form = EditProfileForm(instance=request.user.profile)
  return render(request, 'edit_profile.html', {
    'user_form': user_form,
    'profile_form': profile_form,
    'user': user, 'profile': profile,
    'title': 'Edit Profile'
  })

@login_required
def post_piece(request):
  form = PieceForm(request.POST, request.FILES)
  if form.is_valid():
    piece = form.save(commit = False)
    piece.user=request.user
    piece.save()
    messages.success(request, 'Your piece has been posted!')
  return HttpResponseRedirect('/user/{}'.format(request.user.username))

def detail(request, piece_id):
  piece = Piece.objects.get(pk=piece_id)
  posts = Post.objects.filter(piece_id=piece_id)
  post_form = PostForm()
  return render(request, 'detail.html', {'piece': piece, 'posts': posts, 'post_form': post_form, 'title': piece.name})

@login_required
def post(request, piece_id):
  form = PostForm(request.POST)
  piece = Piece.objects.get(pk=piece_id)
  if form.is_valid():
    post = form.save(commit = False)
    post.user=request.user
    post.piece_id=piece.id
    post.save()
  return HttpResponseRedirect('/{}'.format(post.piece_id))

@login_required
@transaction.atomic 
def edit_piece(request, piece_id):
  piece = Piece.objects.get(pk=piece_id)
  if request.method == 'POST':
    form = EditPieceForm(request.POST, request.FILES, instance=piece)
    if form.is_valid():
      delete_piece = form.cleaned_data['delete_piece']
      if delete_piece:
        piece.delete()
        messages.success(request, 'Your piece was successfully deleted')
        return HttpResponseRedirect('/user/{}'.format(request.user.username))
      else:
        piece_updated = form.save(commit = False)
        piece_updated.user=request.user
        piece_updated.save()
        messages.success(request, 'Your piece was successfully updated!')
        return HttpResponseRedirect('/{}'.format(piece.id))
    else:
      messages.error(request, 'Please make sure you entered changes correctly')
  else:
    form = EditPieceForm(instance=piece)
  return render(request, 'edit_piece.html', {'form': form, 'piece': piece, 'title': ('Edit ' + piece.name)})

def like_piece(request):
  piece_id = request.GET.get('piece_id', None)

  likes = 0
  if (piece_id):
    piece = Piece.objects.get(id=int(piece_id))
    if piece is not None:
      likes = piece.likes + 1
      piece.likes = likes
      piece.save()
  return HttpResponse(likes)
