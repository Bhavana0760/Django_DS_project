# recommendations/forms.py
from django import forms

class RecommendForm(forms.Form):
    height = forms.FloatField(label='Height (cm)')
    weight = forms.FloatField(label='Weight (kg)')
