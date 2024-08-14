from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from.forms import SchoolForm, schoolform
from.models import School, SchoolReg
# Create your views here.
def login(request):
    if request.method == "POST":
        lg_form = SchoolForm(request.POST)
        if lg_form.is_valid():
            try:
                return render("/")
            except:
                pass

    else:
        lg_form = SchoolForm()
        return render (request, "loginpage.html",{"lg_form" : lg_form})
    
def logform(request):
    if request.method == "POST":
        userName = request.POST.get("userName")
        password = request.POST.get("password")

        data = School(userName = userName, password = password)
        data.save()

        template=loader.get_template("resume.html")
        return HttpResponse(template.render())
    
def reg(request):
    if request.method == "POST":
        rg_form = schoolform(request.POST)
        if rg_form.is_valid():
            try:
                return render("/")
            except:
                pass
    else:
        rg_form = schoolform()
        return render(request, "regpage.html", {"rg_form" : rg_form})
    
def regForm(request):
    if request.method == "POST":
        fName = request.POST.get("fName")
        sName = request.POST.get("sName")
        userName = request.POST.get("userName")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")
        re_password = request.POST.get("re_password")

    data = SchoolReg(fName = fName, sName = sName, userName = userName, phone = phone, email = email, password = password, re_password = re_password)
    data.save()
    template=loader.get_template("loginpage.html")
    return HttpResponse(template.render())
def resume(request):
    template= loader.get_template("resume.html")
    return HttpResponse(template.render())