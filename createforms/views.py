from django.shortcuts import render
from .forms import Studentform, snippetform

# Create your views here.
def home(request):

    if request.method == 'POST':
        student = Studentform(request.POST)
        if student.is_valid():
            name = student.cleaned_data['name']
            email = student.cleaned_data['email']
            print(name, email)
    student = Studentform()
    return render(request, "home.html", {'form': student})

def snippet_details(request):
    if request.method == 'POST':
        form = snippetform(request.POST)
        if form.is_valid():
           form.save()
    form = snippetform()
    return render(request, "home.html", {'form': form})
