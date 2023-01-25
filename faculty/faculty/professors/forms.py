from django import forms

from .models import Professor


# Create your forms here.

class RegistrationForm(forms.Form):
    jmbg = forms.CharField(label='JMBG')
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')

    def save(self):
        data = self.cleaned_data
        professor = Professor(jmbg=data['jmbg'], first_name=data['first_name'], last_name=data['last_name'])
        professor.save()

    def all(self):
        return Professor.objects.all()
