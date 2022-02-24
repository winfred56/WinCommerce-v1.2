from django.shortcuts import render, redirect
from .models import UserBase
from django.contrib.auth import login, logout
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from .forms import RegistrationForm, EditDetailsForm


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
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
            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            message = render_to_string('accounts/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            })
            user.email_user(subject, message)
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.object.get(pk=uid)
    except():
        pass
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('shop:home')
    else:
        return render(request, 'account/activation_invalid.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def edit_details(request):
    if request.method == 'POST':
        form = EditDetailsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = EditDetailsForm(instance=request.user)
    return render(request, 'accounts/edit_details.html', {'form': form})
