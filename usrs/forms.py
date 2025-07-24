from allauth.account.forms import SignupForm
from django import forms
from usrs.models import User

class CustomSignupForm(SignupForm):
    name = forms.CharField(max_length=150, label='Name')
    user_type = forms.ChoiceField(choices=[('owner', 'Turf Owner'), ('player', 'Player')], label='User Type')

    def save(self, request):
        user = super().save(request)
        user.name = self.cleaned_data.get('name')
        user.user_type = self.cleaned_data.get('user_type')
        user.save(update_fields=['name', 'user_type'])
        return user 