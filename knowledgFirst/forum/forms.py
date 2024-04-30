from django import forms
from django.forms import ModelForm

from .models import Profile
from django.contrib.auth.models import User

class CategoryChoices(forms.Form):
    CATEGORY_CHOICES = [
        ('Sport', 'Sport'),
        ('Nature', 'Nature'),
        ('Food', 'Food'),
        ('Fashion', 'Fashion'),
        ('Animals', 'Animals'),
        ('Technology', 'Technology'),
        ('Science', 'Science'),
        ('Culture', 'Culture'),
        ('Music', 'Music'),
        ('Entertainment', 'Entertainment'),
        ('History', 'History'),
        ('Fiction', 'Fiction'),
        ('Art', 'Art'),
        ('Other', 'Other')
    ]

    my_field = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.RadioSelect)

class UserUpdateForm(ModelForm):
    class Meta():
        model = User
        fields = ['username']

class ProfileUpdateForm(ModelForm):

    class Meta():
        model = Profile
        fields = ['email', 'avatar']
    
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].required = False