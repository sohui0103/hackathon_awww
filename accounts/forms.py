from django.contrib.auth.forms import UserCreationForm
from awww.models import CustomUser, Profile
from django import forms


#회원가입
class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'password2', 'nickname']

#마이페이지
class ProfileUpdateForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['intro','profile_image']

        widgets = {
            'intro': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_image' : forms.ClearableFileInput(attrs={'class': 'form-control-file', 'onchange': 'readURL(this);'}),
        }

        labels = {
            'profile_image': '프로필 사진',
            'intro': '인사말',
        }
        