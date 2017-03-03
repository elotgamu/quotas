from django import forms


from .models import Printer


class Printercreation_form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.email = kwargs.pop('email')
        super(Printercreation_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Printer
        fields = (
            'name',
            'address',
            'email',
            'phone',
            'bio',
            'tag_line',
            'facebook',
            'twitter',
            'google_plus',
            'linkedin',
        )
        exclude = (
            'user',
            'logo',
            'slug',
        )
