from django import forms
from django.forms.widgets import NumberInput
from django.core import validators
import datetime
from . models import modelClass

class MyForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.Textarea(attrs={'placeholder':'Enter Your Name', 'rows':1}), error_messages={'required':"Please Enter Your Name"})
    age = forms.IntegerField(label="Age", widget=forms.Textarea(attrs={'placeholder':'Enter Your Age', 'rows':1}), validators=[validators.MaxValueValidator(18, "You cannot be a school student")])
    grade = forms.IntegerField(label="Grade", widget=forms.Textarea(attrs={'placeholder':'Enter Your Grade', 'rows':1}))
    email = forms.EmailField(label="Email")
    date = forms.DateField(label="BirthDay", initial=datetime.date.today(), widget=NumberInput(attrs={'type':'date'}), required=False)
    #date = forms.DateField(label="BirthDay", widget=forms.DateInput(attrs={'type':'date'}))
    
    passing_YEAR_CHOICES = ['2023', '2025', '2026']
    passing_year = forms.DateField(label="SSC Passing Year", widget=forms.SelectDateWidget(years=passing_YEAR_CHOICES))
    
    hobbies = [
        ("playing", "Playing"),
        ("reading Books", "Reading Books"),
        ("gardening", "Gardening"),
    ]
    hobby = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=hobbies)

    groups = [
        ("science", "Science"),
        ("commerce", "Commerce"),
        ("arts", "Arts"),
    ]

    group = forms.ChoiceField(label="Select Your Group", choices=groups, widget=forms.RadioSelect)

    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':10}), required=False)
    agree = forms.BooleanField(label="Are You Human?")


    def clean(self):
        cleaned_data = super().clean()
        valage = cleaned_data.get['age']
        if valage < 4:
            raise forms.ValidationError("You Cannot be Student!")

class modelClass(forms.ModelForm):
    class Meta:
        model = modelClass
        fields = '__all__'

        labels = {
            "number":"Number",
            "date_field":"Date",
        }

        widgets = {
            "number":forms.Textarea(attrs={'placeholder':"Enter a big Number as you can", "rows":1}),
            "name":forms.Textarea(attrs={'placeholder':"Enter your name", "rows":1}),
            "date_field":forms.DateInput(attrs={'type':'date'}),
        }

        error_messages = {
            'name' : {'required':'Your name is Required'},
            'boolean_field' : {'required':'Your name is Required'},
        }