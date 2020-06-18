from django import forms
from .models import *


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'

        ExerciseDate = forms.DateField(
            widget=forms.DateInput(format='%m/%d/%Y'),
            input_formats=('%m/%d/%Y')
        )