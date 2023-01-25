from django import forms

from .models import Student


# Create your forms here.

class RegistrationForm(forms.Form):
    jmbg = forms.CharField(label='JMBG')
    index = forms.CharField(label='Index')
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')

    def save(self):
        data = self.cleaned_data
        student = Student(jmbg=data['jmbg'], index=data['index'], first_name=data['first_name'], last_name=data['last_name'])
        student.save()

    def all(self):
        return Student.objects.all()
