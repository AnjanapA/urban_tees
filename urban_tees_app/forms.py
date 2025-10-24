from django import forms
from .models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['email', 'password']

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email',
                'style': 'background-color:black; color:white; border:2px solid red; '
                         'border-radius:6px; padding:10px; width:100%;'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter password',
                'style': 'background-color:black; color:white; border:2px solid red; '
                         'border-radius:6px; padding:10px; width:100%;'
            }),
        }


class SendOTPForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'email']
        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username',
                'style': 'background-color:black; color:white; border:2px solid red; '
                'border-radius:6px; padding:10px; width:100%;'

            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email',  
                'style': 'background-color:black; color:white; border:2px solid red; '
                'border-radius:6px; padding:10px; width:100%;'

            }),
        }


class VerifyOTPForm(forms.Form):
    otp = forms.CharField(
        max_length=6,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter OTP',
                'style': 'background-color:black; color:white; border:2px solid red; '
                'border-radius:6px; padding:10px; width:100%;'
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
                'placeholder': 'Enter password',
                'style': 'background-color:black; color:white; border:2px solid red; '
                'border-radius:6px; padding:10px; width:100%;'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number',
                'style': 'background-color:black; color:white; border:2px solid red; '
                'border-radius:6px; padding:10px; width:100%;'
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
