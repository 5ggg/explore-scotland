from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from explore_scotland_app.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
        
class UserFormWithoutPassword(UserForm):
    def __init__(self, *args, **kwargs):
        super(UserFormWithoutPassword, self).__init__(*args, **kwargs)
        self.fields.pop('password')