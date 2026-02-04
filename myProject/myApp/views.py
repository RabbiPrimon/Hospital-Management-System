from django.shortcuts import render,redirect
from myApp.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


@login_required
def homePage(request):
    
    
    return render(request,"homePage.html")


@login_required
def doctorPage(request):
    
    if request.method=="POST":
        name=request.POST.get("name")
        specialty=request.POST.get("specialty")
        Departmet_id=request.POST.get("Departmet_id")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        doctor_image=request.FILES.get("doctor_image")
        
        departmentName=DepartmentModel.objects.get(id=Departmet_id)
        
        data=DoctorModel(
            DoctorName=name,
            Specialization=specialty,
            phone=phone,
            email=email,
            department=departmentName,
            doctor_image=doctor_image,
        )
        
        data.save()
        
        return redirect("doctorPage")
    
    doctors=DoctorModel.objects.all()
    departments=DepartmentModel.objects.all()
    
    context={
        'doctors':doctors,
        'departments':departments
    }
    
    return render(request,"doctorPage.html",context)


@login_required
def DoctordeletePage(request,id):
    
    data= DoctorModel.objects.get(id=id).delete()
    
    return redirect("doctorPage")
    

@login_required
def DoctoreditPage(request,id):
    departments=DepartmentModel.objects.all()
    doctor=DoctorModel.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("name")
        specialty=request.POST.get("specialty")
        Departmet_id=request.POST.get("Departmet_id")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        departmentName=DepartmentModel.objects.get(id=Departmet_id)

        data=DoctorModel(
            id=id,
            name=name,
            specialization=specialty,
            phone=phone,
            email=email,
            department=departmentName,
        )

        data.save()
        return redirect("doctorPage")
    context={
        'departments':departments,
        'doctor':doctor,
    }
    return render(request,"DoctoreditPage.html",context)


@login_required
def patientPage(request):
    
    doctors=DoctorModel.objects.all()
    patients=PatientModel.objects.all()
    
    
    if request.method=="POST":
        PatientName=request.POST.get("PatientName")
        doctor_id=request.POST.get("doctor_id")
        doctor_name=DoctorModel.objects.get(id=doctor_id)
        address=request.POST.get("address")
    
        email=request.POST.get("email")
        gender=request.POST.get("gender")
        age=request.POST.get("age")
        
        data=PatientModel(
            doctor=doctor_name,
            Address=address,
            email=email,
            Age=age,
            Gender=gender,
            PatientName=PatientName
        )
        data.save()
        return redirect("patientPage")
    
    context={
        'doctors':doctors,
        'patients':patients
    }
    
    
    return render(request,"patientPage.html",context)


@login_required
def appointmentPage(request):
    doctors= DoctorModel.objects.all()
    patients= PatientModel.objects.all()
    appointments=AppointmentModel.objects.all()

    if request.method == "POST":
        
        patient=PatientModel.objects.get(id=request.POST.get("patient"))
        doctor=DoctorModel.objects.get(id=request.POST.get("doctor_id"))
        appointment_date=request.POST.get('appointment_date')


        AppointmentModel.objects.create(
            patient = patient,
            doctor = doctor,
            appointment_date = appointment_date,
        )
    
        

    context = {
       "appointments":appointments,
        "doctors":doctors,
        "patients":patients,


    }
    
    
    return render(request,"appointmentPage.html",context)



@login_required
def departmentPage(request):
    
    
    return render(request,"departmentPage.html")


def loginPage(request):

    if request.method =='POST':
        user_name= request.POST.get("username")
        pass_word= request.POST.get("password")

        user = authenticate(request,username=user_name,password=pass_word)

        if user:
            login(request,user)
            return redirect('homePage')
    
    return render(request,"loginPage.html")

def signupPage(request):

    if request.method=='POST':
        user= request.POST.get('user')
        username= request.POST.get('username')
        email= request.POST.get('Email')
        password= request.POST.get('password')
        Confirm_Password= request.POST.get('Confirm_Password')
        if password==Confirm_Password:
            if customUser.objects.filter(username=username).exists():
                return render(request,"signupPage.html", {"error": "Username already exists"})
            customUser.objects.create_user(
            User_Type = user,
            username = username,
            email= email,
            password= Confirm_Password

        )
        subject = "New_mail"
        message = "Email sent successfully."
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,
        )
        return redirect("loginPage")
    return render(request,"signupPage.html")

def logoutPage(request):
    logout(request)
    return redirect("loginPage")