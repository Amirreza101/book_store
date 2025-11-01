from django.http import HttpRequest, Http404
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, ListView

User = get_user_model()
from django.urls import reverse
from .forms import RegisterForm, LoginForm
from . import forms
from django.utils.crypto import get_random_string


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'accounts/signup.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_username = register_form.cleaned_data.get('username')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
            else:
                new_user = User(
                    email=user_email,
                    username=user_username,
                    email_active_code=get_random_string(72),
                    is_active=False
                )
                new_user.set_password(user_password)
                new_user.save()
                return redirect(reverse('login-page'))

        context = {
            'register_form': register_form
        }

        return render(request, 'accounts/signup.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }

        return render(request, 'accounts/login.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                is_password_correct = user.check_password(user_pass)
                if is_password_correct:
                    login(request, user)
                    return redirect(reverse('home'))
                else:
                    login_form.add_error('email', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'login_form': login_form
        }

        return render(request, 'accounts/login.html', context)


class ProfileView(View):
    def get(self, request):
        user = User.objects.first()
        return render(request, 'accounts/profile.html', context={'account': user})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home'))

    def post(self, request):
        logout(request)
        return redirect(reverse('home'))


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # todo: show success message to user
                return redirect(reverse('login_page'))
            else:
                # todo: show your account was activated message to user
                pass

        raise Http404
