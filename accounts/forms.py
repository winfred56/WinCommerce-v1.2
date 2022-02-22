from django import forms
from .models import UserBase


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
