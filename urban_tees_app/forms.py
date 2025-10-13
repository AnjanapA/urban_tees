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

from django import forms
from .models import User  # Assuming this is a custom User model


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
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


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password','confirm_password' ,'phone','role']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
            }),
            'confirm_password' :forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm password'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),
            'role': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username'
            }),
            
        }

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
