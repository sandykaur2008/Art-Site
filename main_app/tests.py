from django.test import TestCase
from django.urls import reverse 
from django.core import mail 
from .forms import RegisterForm, PieceForm, PostForm, EditProfileForm, EditPieceForm
from .models import Profile, Piece, Post 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# pylint: disable=E1101

# Create your tests here.
class ViewTests(TestCase):
  def test_200(self):
    response1 = self.client.get(reverse('index'))
    response2 = self.client.get(reverse('contact'))
    self.assertEqual(response1.status_code, 200)
    self.assertEqual(response2.status_code, 200)

  def test_404(self):
    response = self.client.get('/made_up_url')
    self.assertEqual(response.status_code, 404)

  def test_302(self):
    response = self.client.post(reverse('contact'), {
      'text': 'some text',
      'email': 'ex@example.com',
      'name': 'some name'})
    self.assertEqual(response.status_code, 302)
    self.assertEqual(len(mail.outbox), 1) 

class FormTests(TestCase):
  def test_form_valid(self):
    form_data_register = {'username': 'fakeuser', 'first_name': 'jane', 'last_name': 'doe', 'email': 'fake@email.com', 'password1': 'georgetown12', 'password2': 'georgetown12'}
    form_register = RegisterForm(data=form_data_register)
    form_data_post = {'body': 'this is a test post'}
    form_post = PostForm(data=form_data_post)
    form_data_piece = {'name': 'test', 'image': 'some_image'}
    form_piece = PieceForm(data=form_data_piece)
    self.assertTrue(form_register.is_valid())
    self.assertTrue(form_post.is_valid())
    self.assertTrue(form_piece.is_valid())

  def test_form_invalid(self):
    form_data_register = {'username': '', 'first_name': 'jane', 'last_name': 'doe', 'email': 'fake@email.com', 'password1': 'georgetown12', 'password2': 'georgetown12'}
    form_register = RegisterForm(data=form_data_register)
    form_data_post = {'body': ''}
    form_post = PostForm(data=form_data_post)
    form_data_piece = {'name': '', 'image': 'some_image'}
    form_piece = PieceForm(data=form_data_piece)
    self.assertFalse(form_register.is_valid())
    self.assertFalse(form_post.is_valid())
    self.assertFalse(form_piece.is_valid())

class ModelTests(TestCase):  
  def setUp(self):
    User.objects.create_user(username='testuser', password='12345')
    self.user = User.objects.get(username='testuser')
    self.profile = Profile.objects.get(user=self.user)
    Piece.objects.create(user=self.user, name='example')
    self.piece = Piece.objects.get(name='example')
    Post.objects.create(user=self.user, piece=self.piece, body='example post')
    self.post = Post.objects.get(body='example post')

  def test_create_instance(self):
    self.assertTrue(isinstance(self.user, User))
    self.assertTrue(isinstance(self.user.profile, Profile))
    self.assertTrue(isinstance(self.piece, Piece))
    self.assertTrue(isinstance(self.post, Post))

  def test_save_instance_edits(self):
    profile_form = EditProfileForm({'bio': 'this is my bio'}, instance=self.profile)
    profile_form.save()
    piece_form = EditPieceForm({'name': 'diff name'}, instance=self.piece)
    piece_form.save()
    self.assertEqual(self.user.profile.bio, 'this is my bio')
    self.assertEqual(self.piece.name, 'diff name')

class LoginView(TestCase):
  def setUp(self):
    self.credentials = {
      'username': 'testuser',
      'password': '12345'}
    User.objects.create_user(**self.credentials)
    self.response = self.client.post(reverse('login'), self.credentials, follow=True)

  def test_login(self):
    self.assertTrue(self.response.context['user'].is_authenticated)

  def test_logout(self):
    self.response = self.client.post(reverse('logout'), self.credentials, follow=True)
    self.assertFalse(self.response.context['user'].is_authenticated)