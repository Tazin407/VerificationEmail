from django import forms
from django.contrib.auth import authenticate, get_user_model

User= get_user_model()

class UserRegisterForm(forms.ModelForm):
    password= forms.CharField(label='Password',widget=forms.PasswordInput)
    confirm_password= forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model= User
        fields= ['email', 'password','confirm_password']
        
    def clean(self, *args, **kwargs):
        email= self.cleaned_data.get('email')
        password= self.cleaned_data.get('password')
        password2= self.cleaned_data.get('confirm_password')
        email_check= User.objects.filter(email=email)
        
        if email_check.exists():
            raise forms.ValidationError('This Email already exists')
        
        if password != password2:
            raise forms.ValidationError('Passwords do not match ')
        
        if len(password) < 5:
            raise forms.ValidationError('Your password should have more than 5 characters')
        return super(UserRegisterForm, self).clean(*args, **kwargs)
   
    
# views.py is going to contain four views needed to send a verification link to verify a user's email. These views include:

# Verify email: send the verification link to the user’s email.
# Verify email done: tell the user to check his/her email.
# Verify email confirm: verify the link.
# Verify email complete: redirect the user to your website after verification.