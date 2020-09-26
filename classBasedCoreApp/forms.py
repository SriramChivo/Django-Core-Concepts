from .models import login, FormModel
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError


class loginForm(ModelForm):
    class Meta:
        model = login
        fields = ['username', 'description', 'about']


class Formclass(forms.Form):
    CHOICES = [('1', 'First'), ('2', 'Second')]
    firstname = forms.CharField(max_length=65, help_text='65 characters max.')
    lastname = forms.CharField(max_length=65, help_text='65 characters max.')
    Age = forms.IntegerField()
    # Choice = forms.CharField(
    #     max_length=65, help_text='65 characters max.', widget=forms.SelectMultiple(choices=CHOICES))
    # choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'loloy'}))
    # nameINTeger = forms.CharField(
    #     widget=forms.NumberInput(attrs={'class': 'loloy'}))
    # url = forms.URLField()
    # comment = forms.CharField(widget=forms.TextInput(attrs={'size': '50'})

    class Meta:
        model = FormModel

    def clean_firstname(self):
        print(len(self.cleaned_data['firstname']))
        print(len(self.cleaned_data['firstname'].strip()))
        cd = self.cleaned_data['firstname'].strip()
        # raise forms.ValidationError("You have forgotten about Fred!")
        return cd


class FormclassModel(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = ['firstname', 'lastname', 'Age']

    def __init__(self, usertext, *args, **kwargs):
        super(FormclassModel, self).__init__(*args, **kwargs)
        self.fields['lastname'].initial = usertext

    # def clean_firstname(self):
    #     raise forms.ValidationError('not valid buddy sorry abt that')
