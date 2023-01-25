import json

import requests
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from .forms import RegistrationForm
from .models import Student


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if check_if_student_exist(form):
                form.save()
            else:
                messages.add_message(request, messages.INFO, 'Student exists in uns database')
    else:
        form = RegistrationForm()

    return redirect('student-list')


def check_if_student_exist(form):
    url = 'http://nginx:80/student'
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
    students = Student.objects.all()
    return render(request, 'students/students.html', {'students': students})
