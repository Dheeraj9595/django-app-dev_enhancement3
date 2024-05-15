# forms.py
from django import forms
from .models import Brand


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # Check if it's an existing instance
            self.fields['upc_ean_gtin'].widget.attrs['readonly'] = True
            self.fields['upc_ean_gtin'].widget.attrs['disabled'] = True
            self.fields['upc_ean_gtin'].help_text = ("This field is not editable. To edit, please create a new Brand "
                                                     "entry.")
