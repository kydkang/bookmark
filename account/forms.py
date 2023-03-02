from django import forms
from django.contrib.auth.models import User 
from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)
    
    class Meta:
        model = User 
        ## You may delete 'first_name' if you are not going to use it. 
        fields = ['username', 'first_name', 'email']  

    def clean_password2(self):
        cd = self.cleaned_data 
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t mathch')
        return cd['password2']
    
    ## To check the uniqueness of email field   
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if not email: 
            raise forms.ValidationError('Email address is required.')
        if email and  User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email addresses must be unique.')
        return email  
    
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    ## To check the uniqueness of email 
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if 'email' in self.changed_data:    ## if email field is changed 
            if email and  User.objects.filter(email=email).exclude(username=username).exists():
                raise forms.ValidationError('Email addresses must be unique.')
        return email  
    
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']

    


