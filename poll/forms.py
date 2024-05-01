from django import forms
from .models import VoterList

class VoterRegistrationForm(forms.ModelForm):
    class Meta:
        model = VoterList
        fields = ['username', 'ph_country_code', 'phone_number', 'photo']

class SignInForm(forms.Form):
    username = forms.CharField(max_length=30)
    photo = forms.ImageField()

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            voter = VoterList.objects.get(username=username)
        except VoterList.DoesNotExist:
            raise forms.ValidationError('Invalid voter.')
        return username
