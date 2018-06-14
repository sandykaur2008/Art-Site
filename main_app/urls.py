from django.urls import path, re_path
from . import views 

urlpatterns = [
    path('', views.index, name = 'index'),
    re_path(r'user/(\w+)/$', views.profile, name = 'profile'),
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'),
    re_path(r'^([0-9]+)/$', views.detail, name = 'detail'),
    path('edit_profile/', views.edit_profile, name = 'edit_profile'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('reset_password/', views.reset_password, name = 'reset_password'),
]