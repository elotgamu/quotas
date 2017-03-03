from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    name = forms.CharField(
        error_messages={'required': 'El campo Nombre es obligatorio'})
    email = forms.CharField(
        error_messages={'required': 'El campo Correo electrónico es obligatorio'}) # noqa
    address = forms.CharField(
        error_messages={'required': 'El campo dirección es obligatorio'})
    phone = forms.CharField(
        error_messages={'required': 'El campo teléfono es obligatorio'})

    class Meta:
        model = Customer
        fields = [
            "name",
            "gender",
            "email",
            "address",
            "phone",
        ]
