from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name='activate'),

    path('login/',
         auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_details/', views.edit_details, name='edit_details'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('delete_confirm/', TemplateView.as_view(template_name='accounts/delete_confirm.html'), name='delete_confirm'),
    path('delete_confirm/', TemplateView.as_view(template_name="account/delete_confirm.html"), name='delete_confirm'),
]
