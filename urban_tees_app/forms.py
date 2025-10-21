from django import forms
from .models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['email', 'password']

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
            }),
        }


class SendOTPForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'email']
        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }),
        }


class VerifyOTPForm(forms.Form):
    otp = forms.CharField(
        max_length=6,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter OTP'
        })
    )

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        ROLE = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]

        fields = [ 'password' ,'phone','role']
        widgets = {
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),
            
        }
        role = forms.ChoiceField(
        choices=ROLE,
        widget=forms.Select()
    )

class UserInfoForm(forms.Form):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    widget={
        'name':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
                    'gender':forms.Select(attrs={
                'class': 'form-control'
            }),
        'address':forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your address',
                'rows': 3
            }),
        
        'place' :forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter place'
            }),
        

        'city' :forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter city'
            }),
        

        'pincode':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter pincode'
            }),
        

        'phone':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            })
    }
