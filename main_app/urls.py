from django.urls import path, re_path
from django.conf import settings 
from django.views.static import serve 
from . import views 

urlpatterns = [
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    re_path(r'^user/(\w+)/$', views.profile, name = 'profile'),
    path('edit_profile/', views.edit_profile, name = 'edit_profile'),
    path('post_piece/', views.post_piece, name='post_piece'),
    re_path(r'^([0-9]+)/$', views.detail, name = 'detail'),
    re_path(r'^post/([0-9]+)/$', views.post, name='post'),
    re_path(r'^edit_piece/([0-9]+)/$', views.edit_piece, name='edit_piece'),
    path('like_piece/', views.like_piece, name = "like_piece")
]


#urlpatterns += [
 # re_path(r'^media/(?P<path>.*)$', serve,
  #{'document_root': settings.MEDIA_ROOT,}),]
    


   