from django.forms import ModelForm
from .models import tutorial

class blogform(ModelForm):
    class Meta:
        model = tutorial
        fields = '__all__'
