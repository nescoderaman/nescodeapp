from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, ListView
from offer_letter import forms
from offer_letter.models import UserProfile

__author__ = 'raman'



@login_required
def profile(request):
    return password_reset(request, template_name='employee_profile.html',
        post_reset_redirect=reverse('success'))


class UpdateEmployeeView(UpdateView):
    model = UserProfile
    template_name = 'add_employee_details.html'
    form_class = forms.employee_profile
    #this is for login required ..without login u can't go to this page
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateEmployeeView, self).dispatch(*args, **kwargs)


    def get_success_url(self):

        return reverse('employee-list1',)

    def get_context_data(self, **kwargs):
        context = super(UpdateEmployeeView, self).get_context_data(**kwargs)
        context['action'] = reverse('employee-edit1',kwargs={'pk':self.get_object().id})

        return context



class ListContactView(ListView):
    model = UserProfile
    template_name = 'employee_list.html'

    #this is for login required ..without login u can't go to this page
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ListContactView, self).dispatch(*args, **kwargs)


from django.core.urlresolvers import reverse
from django.views.generic import CreateView

#inserting of data through this create employee view class.

class CreateEmployeeView(CreateView):
    model = UserProfile
    template_name = 'add_employee_details.html'

    form_class = forms.EmployeeForm
    #this is for login required ..without login u can't go to this page
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateEmployeeView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('employee-list1')

    def get_context_data(self, **kwargs):
        context = super(CreateEmployeeView, self).get_context_data(**kwargs)
        context['action'] = reverse('employee-new1')

        return context
