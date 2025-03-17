from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    # class Person(models.Model):
       first_name = models.CharField(max_length=30,null=False)
       last_name = models.CharField(max_length=30)
       email = models.EmailField(max_length=50, unique=True)
       phone_number = models.CharField(max_length=10, unique=True)
       salary = models.IntegerField(default=0)
       bonus = models.IntegerField(default=0)
       department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
       role = models.ForeignKey(Role, on_delete=models.CASCADE,null=True)
       location = models.CharField(max_length=100,default=0)
       hire_date = models.DateField(auto_now_add=True)

       def __str__(self):
          return f" {self.first_name} {self.last_name} {self.role.name} ({self.department.name})"