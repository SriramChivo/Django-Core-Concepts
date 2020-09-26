from django.forms import ModelForm, Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django import forms
from .models import AdditionalUserInfo, Blog


class Signup(UserCreationForm):

    email = forms.CharField(label="Email :",
                            max_length=120,
                            help_text="Email is Mandatory..",
                            validators=[RegexValidator(
                                regex=r"^[A-Za-z0-9@.]*$", message="Sorry Email is Not valid", code="Invalid Code")],
                            widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    username = forms.CharField(label="Username :",
                               max_length=120,
                               help_text="Username is Mandatory And to be Unique..",
                               validators=[RegexValidator(
                                   regex=r"^[A-Za-z0-9]*$", message="Sorry Username is Not valid")],
                               widget=forms.TextInput(attrs={'placeholder': 'Username', 'size': '30'}))

    password1 = forms.CharField(label='Password1: ',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password2: ', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        print(email)
        return email

# Extend the UserModel with OneToOneField...
# Create a model for creating forms here


class AdditionInfoForm(ModelForm):

    Hobby = forms.CharField(max_length=10, label='Hobby/hobbies: ',
                            validators=[RegexValidator(
                                r'^[a-zA-Z]*$', "Alphabets Only Accepted")],
                            widget=forms.TextInput(attrs={'placeholder': 'Hobbies'}))
    Favourite_Sport = forms.CharField(max_length=10, label='FavouriteSport: ',
                                      validators=[RegexValidator(
                                          r'^[a-zA-Z]*$', "Alphabets Only Accepted")],
                                      widget=forms.TextInput(attrs={'placeholder': 'FavouriteSport'}))
    Working_Place = forms.CharField(max_length=10, label='Working_Place: ',
                                    validators=[RegexValidator(
                                        r'^[a-zA-Z]*$', "Alphabets Only Accepted")],
                                    widget=forms.TextInput(attrs={'placeholder': 'Working_Place', 'size': '35'}))
    Company = forms.CharField(max_length=10, label='Company: ',
                              validators=[RegexValidator(
                                  r'^[a-zA-Z0-9]*$', "Alphabets Only Accepted")],
                              widget=forms.TextInput(attrs={'placeholder': 'Company'}))
    Experience = forms.CharField(max_length=10, label='Experience: ',
                                 validators=[RegexValidator(
                                     r'^[0-9]*$', "Numbers Only Accepted")],
                                 widget=forms.TextInput(attrs={'placeholder': 'Experience'}))

    class Meta:
        model = AdditionalUserInfo
        fields = ['Hobby', 'Favourite_Sport',
                  'Working_Place', 'Experience', 'Company']  # Above fields created only to the fields defined in the list..


class createForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['Item', 'description']
