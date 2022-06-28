from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  
    
    # path('login/', views.login, name='login'),
     #path('validate_login/', views.login_validate, name='login_validate'),
     path('forget_password/', views.forget_password, name='forget_password'),
     path('register/', views.usersignup, name='register'),
     #path('activate/<uidb64>/<token>/', views.activate, name='activate'),




           path('login/', auth_views.LoginView.as_view(template_name= 'iroomie/login-page.html'), name='login'),
           path('logout/', auth_views.LogoutView.as_view(next_page= 'login'), name='logout'),

           #path('google/', include('social_django.urls', namespace='social')),

         path('password_reset/', auth_views.PasswordResetView.as_view(
           template_name= 'iroomie/passwordreset/password_reset.html',
           subject_template_name ='iroomie/passwordreset/password_reset_subject.txt',
           email_template_name = 'iroomie/passwordreset/password_reset_email.html',
           #2success_url = '/login/'
           ),
           name='password_reset'),
         path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(
           template_name= 'iroomie/passwordreset/password_reset_done.html'),
           name='password_reset_done'),

         path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
           template_name= 'iroomie/passwordreset/password_reset_confirm.html'),
           name='password_reset_confirm'),


         path('password_reset/complete/',auth_views.PasswordResetCompleteView.as_view(
           template_name= 'iroomie/passwordreset/password_reset_complete.html'),
           name='password_reset_complete'),
   
   ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


