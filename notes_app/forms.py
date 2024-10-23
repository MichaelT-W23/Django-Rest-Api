from django import forms

class UserForm(forms.Form):
    username = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(),
        error_messages={
            'required': 'Username is required.',
            'max_length': 'Username cannot exceed 80 characters.'
        }
    )

    email = forms.EmailField(
        required=True,
        max_length=120,
        widget=forms.EmailInput(),
        error_messages={
            'required': 'Email is required.',
            'invalid': 'Enter a valid email address.',
            'max_length': 'Email cannot exceed 120 characters.'
        }
    )

    password = forms.CharField(
        required=True,
        min_length=6,
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Password is required.',
            'min_length': 'Password must be at least 6 characters long.'
        }
    )


class UserLoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(),
        error_messages={
            'required': 'Username is required.',
            'max_length': 'Username cannot exceed 80 characters.'
        }
    )
    
    password = forms.CharField(
        required=True,
        min_length=6,
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Password is required.',
            'min_length': 'Password must be at least 6 characters long.'
        }
    )
