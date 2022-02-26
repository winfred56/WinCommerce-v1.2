from django import forms
from .models import UserBase
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(min_length=4, max_length=50, label='Username', help_text='required')
    email = forms.EmailField(max_length=100, label='email', help_text='required', error_messages={
        'required': 'You must enter an email address'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput, help_text='required')
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput, help_text='required')

    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)

    def clean_password2(self):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('Passwords do not match')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update({
            'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({
            'class': 'form-control mb-3', 'placeholder': 'Email', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update({
            'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control mb-3', 'placeholder': 'Repeat Password'})


class LoginForm(AuthenticationForm):
    user_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Password', 'id': 'login-pwd',
    }))


class EditDetailsForm(forms.ModelForm):
    user_name = forms.CharField(label='Username', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'form-user_name'}))
    full_name = forms.CharField(label='Full name', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Full name', 'id': 'form-lastname'}))
    email = forms.EmailField(label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email', 'readonly': 'readonly'}))

    class Meta:
        model = UserBase
        fields = ('email', 'user_name', 'full_name',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['user_name'].required = True
            self.fields['email'].required = True


class PwdResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        check_email = UserBase.object.filter(email=email)
        if not check_email:
            raise forms.ValidationError('Enter a correct email address')
        return email
