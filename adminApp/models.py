from django.db import models
from django.contrib.auth.models import User

class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USER_LIST = [("admin", 'Admin'), ('student', 'Student'), ('staff', 'Staff')]
    user_type = models.CharField(max_length=255, choices=USER_LIST, default='student')
    
    def __str__(self):
        return self.user.first_name
    


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    duration = models.PositiveIntegerField()  
    

    def __str__(self):
        return self.name
    

class Division(models.Model):
    name = models.CharField(max_length=50, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.name} - {self.course.name}"
    


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_number = models.CharField(max_length=20, unique=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True, blank=True) 
    guardian_name = models.CharField(max_length=100, null=True, blank=True)
    guardian_phone = models.CharField(max_length=15, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.enrollment_number}"
    

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    designation = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    joining_date = models.DateField()
    is_gfm = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"