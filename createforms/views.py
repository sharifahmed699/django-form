from django.shortcuts import render
from .forms import Studentform

# Create your views here.
def home(request):

    if request.method == 'POST':
        student = Studentform(request.POST)
        if student.is_valid():
            name = student.cleaned_data['name']
            email = student.cleaned_data['email']
            print(name, email)

    return render(request, "home.html", {'form': student})