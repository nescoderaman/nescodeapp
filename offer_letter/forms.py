from reportlab.lib.units import inch
from reportlab.lib import styles
from django.utils.translation import ugettext_lazy as _
from django.views.generic import UpdateView

__author__ = 'raman'
from django import forms
from offer_letter.models import offer1


class EmployeeForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)),label=_("Name Of Employee :"))
    empid = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)),label=_("Employee Id :"))
    doj = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)),label=_("Date Of Joining :"))
    designation = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                  label=_("Designation :"))
    company = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)),label=_("Company :"))
    supervisername = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                    label=_("Superviser Name :"))
    ctc = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)),label=_("CTC :"))
    traning_duration = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                        label=_("Traning Duration :"))
    leave = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                        label=_("Leave :"))
    add1 = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                        label=_("Address Line 1 :"))
    add2 = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                        label=_("Address Line 2 :"))
    add3 = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                        label=_("Address Line 3 :"))

    class Meta:
        model = offer1

