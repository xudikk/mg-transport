from core.models import Department
from django import forms


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
