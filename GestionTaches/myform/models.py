from django.contrib import admin
from django.db import models
from django import forms
from django.shortcuts import render
from django.forms.fields import DateField, ChoiceField,MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple


class Contact(models.Model):
    name = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.CharField(max_length=1000)


class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)



BIRTH_YEAR_CHOICES = ('1999', '2000', '2001')
GENDER_CHOICES = (('m', 'Male'), ('f', 'Female'))
FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),
('green', 'Green'),
('black', 'Black'))
class SimpleForm(forms.Form):
    birth_year = DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    gender = ChoiceField(widget=RadioSelect, choices=GENDER_CHOICES)
    favorite_colors = forms.MultipleChoiceField(required=False,
    widget=CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)

    class CommentForm(forms.Form):
        name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'special'}))
        url = forms.URLField()
        comment = forms.CharField(
        widget=forms.TextInput(attrs={'size':'40'}))

