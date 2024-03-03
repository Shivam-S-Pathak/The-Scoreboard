from django import forms

class ResultForm(forms.Form):
    course = forms.CharField(max_length=100)
    semester = forms.IntegerField()
    exam_type = forms.CharField(max_length=100)