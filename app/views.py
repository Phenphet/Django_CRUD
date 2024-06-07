from django.shortcuts import render, redirect, HttpResponse
from .models import Student
from .forms import StudentForm

# Create your views here.
def home(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'app/home.html', context)

def createHome(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = StudentForm()

    else: 
        form = StudentForm()

    context = {'form': form} 
    return render(request, 'app/home_from.html', context)

def editHome(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance= student)

        if form.is_valid():
            form.save()
            return redirect ('home')
        
        else:
            form = StudentForm(instance= student)

    else:
        form = StudentForm(instance= student)

    context = {'form': form}

    return render(request, 'app/edit.html', context)

def detailHome(request, id):
    students = Student.objects.filter(id=id)
    context = {'students': students}
    return render(request, 'app/detail.html', context)

def deleteHome(request, id):
    student = Student.objects.get(id=id)
    student.image.delete()
    student.delete()
    return redirect('home')