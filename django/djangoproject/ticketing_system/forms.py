from django import forms

class TestForm(forms.Form):
    subjectTest = forms.CharField(max_length=100)