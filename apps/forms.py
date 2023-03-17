from django import forms

from .models import Users


class UsersForm(forms.ModelForm):
    username = forms.CharField(max_length=255)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    job = forms.CharField(max_length=255)
    location = forms.CharField(max_length=255)
    gmail = forms.EmailField()
    phone = forms.CharField(max_length=11)
    birthday = forms.DateField()
    image = forms.ImageField()

    class Meta:
        model = Users
        fields = ('username', 'first_name', 'last_name', 'job', 'location', 'gmail', 'phone', 'birthday', 'image')
