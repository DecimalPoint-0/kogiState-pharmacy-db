from cProfile import label
from django.forms import TextInput, Select, FileInput, NumberInput, Textarea, CheckboxSelectMultiple
from django.forms import ModelForm
from .models import Pharmacy
from django import forms

class PharmacyForm(ModelForm):
    class Meta:
        model = Pharmacy
        fields = '__all__'