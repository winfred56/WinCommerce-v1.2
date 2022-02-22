from django.shortcuts import render
from .models import UserBase
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_name = form.cleaned_data['user_name']
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()
            # activation Email
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})




