from django.contrib import admin
from myApp.models import *


admin.site.register(DepartmentModel)
admin.site.register(DoctorModel)
admin.site.register(PatientModel)
admin.site.register(AppointmentModel)
admin.site.register(customUser)