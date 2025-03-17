from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from datetime import datetime
# from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context={
        'emps':emps

    }
    print(context)
    return render(request, 'all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number =int(request.POST['phone_number'])
        email =request.POST['email']
        role = request.POST['role']
        department = request.POST['department']
        location = request.POST['location']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        
        # Retrieve the Role instance based on the provided name
        try:
            role = Role.objects.get(name=role)  # Get the Role instance by name
        except Role.DoesNotExist:
            return HttpResponse(f"Role '{role}' not found.", status=400)

        # Retrieve the Department instance based on the provided name
        try:
            department = Department.objects.get(name=department)  # Get the Department instance by name
        except Department.DoesNotExist:
            return HttpResponse(f"Department '{department}' not found.", status=400)


        new_emp = Employee(first_name=first_name,last_name=last_name,phone_number=phone_number,email=email,role=role,department=department,location=location,salary=salary,bonus=bonus)
        new_emp.save()  
        return HttpResponse('Employee Added Successfully')
    
    elif request.method == 'GET':
        return render(request,'add_emp.html')
    
    else:
       return HttpResponse('Invalid Request')

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp = Employee.objects.get(id=emp_id)
            emp.delete()
            return HttpResponse('Employee Removed Successfully')
        except Employee.DoesNotExist:
            return HttpResponse('Employee Not Found')
    
    emps = Employee.objects.all()
    context={
        'emps':emps
        }
    
    return render(request, 'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        role = request.POST['role']
        department = request.POST['department']
        location = request.POST['location']
        emps = Employee.objects.all()
        
        if first_name:
            emps = Employee.objects.filter(first_name__icontains=first_name)
        if last_name:
            emps = emps.filter(last_name__icontains=last_name)
        if department:
            emps = emps.filter(department__name__icontains=department)
        if role:
            emps = emps.filter(role__name__icontains=role)
        if location:
            emps = emps.filter(location__name__icontains=location)

        context = {
            'emps':emps
        }
        
        return render(request, 'all_emp.html',context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    
    else:
        return HttpResponse('Invalid Request')
  

