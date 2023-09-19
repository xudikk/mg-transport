from django import forms

from core.models import AutoBrand, AutoMotoTransport, AutoMotoTransportModel, AutoMotoTransportColor


class AutoBrandForm(forms.ModelForm):
    class Meta:
        model = AutoBrand
        fields = '__all__'


class AutoModelForm(forms.ModelForm):
    class Meta:
        model = AutoMotoTransportModel
        fields = '__all__'


class AutoColorForm(forms.ModelForm):
    class Meta:
        model = AutoMotoTransportColor
        fields = '__all__'


class AutoMotoForm(forms.ModelForm):
    class Meta:
        model = AutoMotoTransport
        fields = '__all__'
