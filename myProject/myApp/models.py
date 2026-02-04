from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):

    USER =[
        ('Doctor','Doctor'),
        ('Patient','Patient'),
    ]

    User_Type= models.CharField(choices=USER,null=True)


class DepartmentModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    location=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class DoctorModel(models.Model):
    SPECIALIZATIONS = [
        ('Cardiology', 'Cardiology'),
        ('Neurology', 'Neurology'),
        ('Orthopedics', 'Orthopedics'),
        ('Pediatrics', 'Pediatrics'),
        ('General Medicine', 'General Medicine'),
        ('Dermatology', 'Dermatology'),
    ]
    name=models.CharField(max_length=100,null=True)
    specialization=models.CharField(max_length=100, choices=SPECIALIZATIONS, null=True)
    phone=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    department=models.ForeignKey(DepartmentModel,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
class PatientModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    age=models.IntegerField(null=True)
    gender=models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], null=True)
    phone=models.CharField(max_length=100,null=True)
    address=models.TextField(null=True)
    doctor=models.ForeignKey(DoctorModel,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
class AppointmentModel(models.Model):
    patient=models.ForeignKey(PatientModel,null=True,on_delete=models.CASCADE)
    doctor=models.ForeignKey(DoctorModel,null=True,on_delete=models.CASCADE)
    appointment_date= models.DateTimeField(null=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Pending')

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"
    








