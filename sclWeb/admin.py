from django.contrib import admin
from.models import School, SchoolReg

# Register your models here.
class SchoolData(admin.ModelAdmin):
    list_display = [
        "userName",
        "password",
    ]
    

admin.site.register(School, SchoolData)

class schooldata(admin.ModelAdmin):
    list_display = [
        "fName",
        "sName",
        "userName",
        "phone",
        "email",
        "password",
        "re_password",
    ]

admin.site.register(SchoolReg, schooldata)