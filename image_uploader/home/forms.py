from django  import forms
from .models import image


class imageForm(forms.ModelForm):
    class Meta:
        model=image
        fields='__all__'
        labels={'photo':''}