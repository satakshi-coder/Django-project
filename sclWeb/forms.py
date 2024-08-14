from.models import School, SchoolReg
from django import forms

class SchoolForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        widget = {
            "password" : forms.PasswordInput()
        }
        model = School
        fields = "__all__"

class schoolform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        widget = {
            "password" : forms.PasswordInput()
        }
        model = SchoolReg
        fields = "__all__"