from django.shortcuts import render,redirect
from .models import StudentData

# Create your views here.
def home(request):
    sd=StudentData.objects.all()
    return render(request,'home.html',{'sd':sd})
def add_student(request):
    if request.method=='GET':
        return render(request,'student_reg.html')
    else:
        StudentData(
            firstname=request.POST.get('fname'),
            lastname=request.POST.get('lname'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            mark1=request.POST.get('mark1'),
            mark2=request.POST.get('mark2'),
            mark3=request.POST.get('mark3'),
            mark4=request.POST.get('mark4')
            ).save()
        sd=StudentData.objects.all()
    return render(request,'home.html',{'sd':sd})    

def update_data(request,id):
    student=StudentData.objects.get(id=id)
    return render(request,'update_data.html',{'student':student})

def save_data(request,id):
    student=StudentData.objects.get(id=id)
    student.firstname=request.POST.get('fname')
    student.lastname=request.POST.get('lname')
    student.email=request.POST.get('email')
    student.mobile=request.POST.get('mobile')
    student.mark1=request.POST.get('mark1')
    student.mark2=request.POST.get('mark2')
    student.mark3=request.POST.get('mark3')
    student.mark4=request.POST.get('mark4')
    student.save()
    return redirect(home)

def delete_data(request,id):
    student=StudentData.objects.get(id=id)
    student.delete()
    return redirect(home)