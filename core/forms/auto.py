import datetime

from django import forms

from core.models import AutoBrand, AutoMotoTransport, AutoMotoTransportModel, AutoMotoTransportColor
from core.models.auto import NotificationModel


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

    def save(self, commit=True, user=None, change_type="add"):
        instance = super(AutoMotoForm, self).save(commit=commit)
        if user and user.ut != 1:
            instance.change = True
            instance.status = 'waiting'
            instance.save()
            notifi = NotificationModel.objects.create(
                last_change=datetime.datetime.now(),
                user=user,
                change_type=change_type,
                transport=instance
            )
            notifi.save()
        else:
            instance.change = False
            instance.status = 'active'
            instance.save()
        return instance
