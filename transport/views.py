from django.shortcuts import render,redirect,get_object_or_404
from .forms import  CreateDepartment
from .models import Department
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = CreateDepartment(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transport:list')
    else:
        form = CreateDepartment()

    context = {"message":"Welcome Note",'form':form}
    return render(request, 'transport/index.html', context)

def list(request):
    data = Department.objects.all()
    context = {"message":"Listing the Departments", "departmentlist":data}
    return render(request, 'transport/list.html', context)

def edit(request,id):
    department = get_object_or_404(Department, pk=id)
    #https://sixfeetup.com/blog/django-form-data-in-post
    if request.method == 'POST':
        data = request.POST.copy()
        department.name = data.get('name')
        department.code = data.get('code')
        department.description = data.get('description')

        form = CreateDepartment(department.__dict__)
        ###using the form to validate the Model######
        if form.is_valid():
            print(department.__dict__)
            department.save()
            return redirect('transport:list')

        else:
            context = {'form': form}
            return render(request, 'transport/edit.html', context)
    else:
        form = CreateDepartment(department.__dict__)
        context = {'form': form}
        return render(request, 'transport/edit.html', context)

def detail(request,id):
    department = get_object_or_404(Department, pk=id)
    context={

        'department': department,

        'message':'Details for '+department.name +'Department'
    }

    return render(request, 'transport/detail.html', context)
