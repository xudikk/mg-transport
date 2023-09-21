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

    def __init__(self, *args, **kwargs):
        root = kwargs.pop('department')
        super().__init__(*args, **kwargs)
        self.fields['department'].initial = root

    def save(self, commit=True):
        instance = super(AutoMotoForm, self).save(commit=commit)
        return instance
