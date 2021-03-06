from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . forms import LoginForm , MyPasswordChangeForm ,MyPasswordResetForm , MySetPasswordForm
from . import views
urlpatterns = [
    path('' , auth_views.LoginView.as_view(template_name='login/login.html' , authentication_form=LoginForm) , name='login'),
    path('logout/' , auth_views.LogoutView.as_view(next_page='login') , name='logout'),
    path('profile/', views.profile , name='profile'),
    path('passwordchange/' , auth_views.PasswordChangeView.as_view(template_name='login/passwordchange.html', form_class=MyPasswordChangeForm ,success_url= '/passwordchangedone/') , name='passwordchange'),
    path('passwordchangedone/' , auth_views.PasswordChangeView.as_view(template_name='login/passwordchangedone.html') , name='passwordchangedone'),
    path('password-reset/' , auth_views.PasswordResetView.as_view(template_name='login/password_reset.html' , form_class=MyPasswordResetForm) , name="password_reset"),
    path('password-reset/done/' , auth_views.PasswordResetDoneView.as_view(template_name='login/password_reset_done.html' ) , name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html' , form_class = MySetPasswordForm ) , name="password_reset_confirm"),
    path('password-reset-complete/' , auth_views.PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html' ) , name="password_reset_complete"),
    path('registration/' , views.CustomerRegistrationView.as_view() , name = "customerregistration")
 
 ]
