from django.urls import path,include
from django.conf.urls import url
from . import views
from django.contrib import auth
from django.contrib.auth import login,views as auth_views
from django.contrib.auth.views import LoginView,LogoutView

from .views import edit_post,edit_done,test,popup



app_name='dailyreport'

urlpatterns = [

   url(r'^$', views.home, name='home'),
   path('report/',views.reportpage2,name='report'),
   path('details/',views.details,name='details'),
   path('repdetail/<int:pk>',popup.as_view(), name='popup-detail'),
   path('search_page/',views.search_page,name='serach_page'),
   path('test/',views.test,name='test'),
   path('details/edit/<int:pk>',edit_post.as_view(), name='edit_post'),
   path('edit_done/',views.edit_done,name='edit_done'),
   #path('login/',views.login_page,name='login_page'),
   path('login/',LoginView.as_view(template_name='registration/worksheet_login.html'),name='login_page' ),
   path('logout/',LogoutView.as_view(template_name='home.html'),name='logout_worksheet'),
   path('loginldap/',views.loginldap,name='login_pageldap' ),
   path('pdftest/',views.pdftest,name='pdftest'),
   
   
   #authentication,login,pass and reser pass
    #path('', auth_views.LoginView.as_view(), {'template_name': 'registration/login.html'}, name = 'login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html')),        
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'), 


 


]