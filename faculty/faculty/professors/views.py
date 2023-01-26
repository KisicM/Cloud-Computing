import json

import requests
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from .forms import RegistrationForm
from .models import Professor


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if check_if_student_exist(form):
                form.save()
    else:
        form = RegistrationForm()

    return redirect('professor-list')


def check_if_student_exist(form):
    #return True
    url = 'http://localhost:3000/users/professors'
    data = {
        'jmbg': form.cleaned_data['jmbg'],
        'name': form.cleaned_data['first_name'] + " " + form.cleaned_data['last_name'],
    }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        return True
    return False


def all_students_view(request):
    professors = Professor.objects.all()
    return render(request, 'professors/professors.html', {'professors': professors})
