from django.urls import path, re_path
from django.conf import settings 
from . import views 

urlpatterns = [
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('', views.index, name = 'index'),
]
    
    # re_path(r'^user/(\w+)/$', views.profile, name = 'profile'),
    # path('contact/', views.contact, name = 'contact'),
    # path('about/', views.about, name = 'about'),
    # re_path(r'^([0-9]+)/$', views.detail, name = 'detail'),
    # path('edit_profile/', views.edit_profile, name = 'edit_profile'),
    # path('reset_password/', views.reset_password, name = 'reset_password'),
    # path('reset_password_request/', views.reset_password_request, name = 'reset_password request'),