from django import forms
from .models import Post,Profile, Business,Neighbourhood

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'name', 'email', 'location', 'occupant_id']

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ['name','post','post_caption','neighbourhood','date']

