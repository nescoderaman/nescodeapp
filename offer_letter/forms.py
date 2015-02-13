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



# for creating candidate as employee

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                label=_("User Name"), error_messages={
            'invalid': _("This value must contain only letters, numbers and underscores.")})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email Address"))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
        label=_("Password (again)"))


    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data



from offer_letter.models import UserProfile
from django.utils.translation import ugettext_lazy as _
class employee_profile(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30,)),label=_(" First "
                                                                                                           "Name :"))
    class Meta:
        model = UserProfile
