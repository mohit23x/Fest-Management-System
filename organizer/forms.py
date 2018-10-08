from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms
from django.forms import ModelForm
from .models import Event, Sponser

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'minimumparticipant', 'maximumparticipant', 'date', 'entries', 'fees']


class UserCreateForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'group']

class addcoordinatortoevenntForm(ModelForm):
   # user = forms.ModelMultipleChoiceField()

    class Meta:
        model = Event
        fields = ['user']


class addsponserForm(ModelForm):
    class Meta:
        model = Sponser
        fields = '__all__'