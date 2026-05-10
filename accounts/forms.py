from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm as DjangoPasswordChangeForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    role = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class PasswordChangeForm(DjangoPasswordChangeForm):
    pass


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'})
    )


class PasswordResetConfirmForm(forms.Form):
    token = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter token from email'})
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New password'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'})
    )

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('new_password')
        p2 = cleaned.get('confirm_password')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('Passwords do not match.')
        return cleaned
