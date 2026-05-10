<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
"""
Accounts App - Palisha
Login, Register, Logout, Profile, Change Password, Password Reset
"""
import secrets
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from core.models import UserProfile, AuditLog, Notification
from organization.models import Department
from .models import PasswordResetToken
from .forms import RegisterForm, ProfileUpdateForm, PasswordChangeForm, PasswordResetRequestForm, PasswordResetConfirmForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            AuditLog.objects.create(user=user, action_type='insert', table_name='Session', description=f'{user.username} logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(user=user, role=request.POST.get('role', ''))
            dept_id = request.POST.get('department')
            if dept_id:
                try:
                    profile.department = Department.objects.get(pk=dept_id)
                except Department.DoesNotExist:
                    pass
            profile.save()
            AuditLog.objects.create(user=user, action_type='insert', table_name='User', record_id=user.id, description=f'New user registered: {user.username}')
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
    else:
        form = RegisterForm()
    departments = Department.objects.all()
    return render(request, 'accounts/register.html', {'form': form, 'departments': departments})


def logout_view(request):
    if request.user.is_authenticated:
        AuditLog.objects.create(user=request.user, action_type='delete', table_name='Session', description=f'{request.user.username} logged out')
    logout(request)
    return redirect('login')


@login_required
def profile_view(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            profile.role = request.POST.get('role', '')
            dept_id = request.POST.get('department')
            if dept_id:
                try:
                    profile.department = Department.objects.get(pk=dept_id)
                except Department.DoesNotExist:
                    pass
            profile.save()
            AuditLog.objects.create(user=request.user, action_type='update', table_name='UserProfile', description='Profile updated')
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    departments = Department.objects.all()
    return render(request, 'accounts/profile.html', {'form': form, 'profile': profile, 'departments': departments})


@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            AuditLog.objects.create(user=request.user, action_type='update', table_name='User', description='Password changed')
            messages.success(request, 'Password changed successfully.')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})


def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                token = secrets.token_urlsafe(32)
                PasswordResetToken.objects.create(user=user, token=token)
                send_mail(
                    subject='Password Reset Token — Broadcast Engineering Teams',
                    message=f'Your password reset token is:\n\n{token}\n\nEnter this on the reset page. It expires after use.',
                    from_email='noreply@broadcast.com',
                    recipient_list=[email],
                    fail_silently=True,
                )
                messages.success(request, f'Reset token sent to {email}. Check console output in development.')
                print(f"\n[DEV] Password reset token for {user.username}: {token}\n")
                return redirect('password_reset_confirm')
            except User.DoesNotExist:
                messages.error(request, 'No account found with that email address.')
    else:
        form = PasswordResetRequestForm()
    return render(request, 'accounts/password_reset.html', {'form': form})


def password_reset_confirm(request):
    if request.method == 'POST':
        form = PasswordResetConfirmForm(request.POST)
        if form.is_valid():
            token_str = form.cleaned_data['token']
            new_password = form.cleaned_data['new_password']
            try:
                token_obj = PasswordResetToken.objects.get(token=token_str, used=False)
                user = token_obj.user
                user.set_password(new_password)
                user.save()
                token_obj.used = True
                token_obj.save()
                AuditLog.objects.create(user=user, action_type='update', table_name='User', description='Password reset via token')
                messages.success(request, 'Password reset successfully. Please log in.')
                return redirect('login')
            except PasswordResetToken.DoesNotExist:
                messages.error(request, 'Invalid or expired token.')
    else:
        form = PasswordResetConfirmForm()
    return render(request, 'accounts/password_reset_confirm.html', {'form': form})


def password_reset_done(request):
    return render(request, 'accounts/password_reset_done.html')

>>>>>>> 1bbd6c5 (Initial project setup)
