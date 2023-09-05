from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationFrom(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required.Enter a valid email address.')

    def check_email(self)
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        
        return email

    class Meta:
        model = User #using the built-in User Model
        fields = ('username', 'email', 'password1', 'password2')

