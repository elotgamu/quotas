from django import forms

from .models import Product, Material


class ProductCreate_Form(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'has_pliegos',
            'is_digital',
            'material',
        )
        exclude = (
            'added_by',
            'creted_on',
            'slug',

        )


class MaterialCreate_Form(forms.ModelForm):

    class Meta:
        model = Material
        fields = (
            'name',
            'description',
        )
