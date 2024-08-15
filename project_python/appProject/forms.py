from django.forms import ModelForm
from .models import ExcelFile

class MyImageForm(ModelForm):
    class Meta:
        model = ExcelFile
        fields = '__all__'