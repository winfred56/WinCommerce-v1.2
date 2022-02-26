from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .forms import PwdResetForm, PwdResetConfirmForm

app_name = 'accounts'
urlpatterns = [
    # user registration
    path('register/', views.register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name='activate'),

    # login & logout
    path('login/',
         auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),

    # user dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_details/', views.edit_details, name='edit_details'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('delete_confirm/', TemplateView.as_view(template_name='accounts/delete_confirm.html'), name='delete_confirm'),
    path('delete_confirm/', TemplateView.as_view(template_name="account/delete_confirm.html"), name='delete_confirm'),

    # Password Reset
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html',
        success_url='password_reset_email_confirm',
        email_template_name='accounts/password_reset_email.html',
        form_class=PwdResetForm), name='password_reset'),

    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        form_class=PwdResetConfirmForm,
        success_url='password_reset_complete/'), name='password_reset_confirm'),

    path('password_reset/password_reset_email_confirm/', TemplateView.as_view(template_name='accounts/reset.html'),
         name='password_reset_done'),
    path('password_reset_confirm/MTc/password_reset_complete/', TemplateView.as_view(
        template_name='accounts/reset.html'), name='password_reset_complete'),

]
