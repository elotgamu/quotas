from django import forms

from .models import Quota


class Quota_Form(forms.ModelForm):

    class Meta:
        model = Quota
        fields = (
            'name',
            'description',
            'quota_type',
            'material',
            'quantity',
            'before_date',
            'size',
            'quiebres',
            'single_side',
        )
