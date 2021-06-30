from django import forms

class InformationForm(forms.Form):
    fname=forms.CharField(max_length=100)
    mname = forms.CharField(max_length=100)
    lname = forms.CharField(max_length=100)
    dob = forms.DateField()
    gender=forms.CharField(max_length=10)
    nationality=forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    state= forms.CharField(max_length=50)
    pin = forms.CharField(max_length=10)
    qualification=forms.CharField(max_length=30)
    salary=forms.IntegerField()
    pan=forms.CharField(max_length=100)





