from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from signup.models import Signup
from employee_details.models import Employee

def disp(request):
    return HttpResponse("Hey this is a response from Django")
def about(request):

    return render(request,'about.html')
def login(request):

    return render(request,'login.html')

    return render(request,'sum.html',{"sum":result})

def signup(request):
    try:
       username = request.POST['username']
       password = request.POST['password']
       sg=Signup(username=username,password=password)
       sg.save()
    except Exception as e:
        print(e)
    return render (request,'signup.html')

def home(request):
    return render(request,'employee.html')

def getallemp(request):
    emp=Employee.objects.all()
    data={
        'emp':emp
    }

    return render(request,'employee.html',data)

def addEmp(request):
    name=request.POST['name']
    email=request.POST['email']
    address=request.POST['address']
    phone=request.POST['phone']

    emp=Employee(name=name,email=email,address=address,phone=phone)
    emp.save()

    return redirect('/emp/')


def editEmp(request):
    emp=Employee.objects.all()

    data={
        'emp':emp
    }


    return render(request,'employee.html',data)

def updateEmp(request,id):
    name=request.POST['name']
    email=request.POST['email']
    address=request.POST['address']
    phone=request.POST['phone']
    emp=Employee(id=id,name=name,email=email,address=address,phone=phone)
    emp.save()

    return redirect('/emp/')

def deleteEmp(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('/emp/')


