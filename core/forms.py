from django import forms
from .models import Job,PersonJobDetail,Person
from django.core.validators import MinValueValidator




class PersonForm(forms.ModelForm):
    first_name=forms.CharField(label='First Name', min_length=3,required=True, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    last_name = forms.CharField(label='Last Name', min_length=3,required=True, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    address = forms.CharField(label='Address', min_length=3,required=True, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    mobile = forms.CharField(label='Mobile', min_length=7,required=True, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    class Meta:
        model = Person
        fields=('first_name','last_name','address','mobile')
  

class JobForm(forms.ModelForm):
    title_ar=forms.CharField(label='Job Title Ar', min_length=3,required=True, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control mb-3','dir': 'rtl'}))
    title_en = forms.CharField(label='Job Title En', min_length=3,required=True, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    min_salary = forms.DecimalField(label='Min salary',max_digits=10,decimal_places=2,required=True, widget=forms.NumberInput(attrs={'class': 'form-control mb-3'}))
    class Meta:
        model = Job
        fields=('title_ar','title_en','min_salary')


    
class PersonJobDetailForm(forms.ModelForm):
    person=forms.ModelChoiceField(label='Select Person',queryset=Person.objects.all(), required=True,widget=forms.Select(attrs={'class': 'form-control mb-3'}))
    job=forms.ModelChoiceField(label='Select Job',queryset=Job.objects.all(), required=True,widget=forms.Select(attrs={'class': 'form-control mb-3'}))
    salary = forms.DecimalField(label='salary',max_digits=10,decimal_places=2,required=True, widget=forms.NumberInput(attrs={'class': 'form-control mb-3'}))
    years_of_experince=forms.IntegerField(label='ُYears Of Experince',required=True,widget=forms.NumberInput(attrs={'class': 'form-control mb-3'}),validators=[MinValueValidator(0)])
    class Meta:
        model = PersonJobDetail
        fields=('person','job','salary','years_of_experince')