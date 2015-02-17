from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from offer_letter import forms
from offer_letter.models import emp
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView
__author__ = 'raman'

class ListContactView(ListView):
    model = emp
    template_name = '/HR/emp_list.html'

    #this is for login required ..without login u can't go to this page
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ListContactView, self).dispatch(*args, **kwargs)




#inserting of data through this create employee view class.

class CreateEmployeeView(CreateView):
    model = emp
    template_name = '/HR/add_emp.html'

    form_class = forms.emp_profile
    #this is for login required ..without login u can't go to this page
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateEmployeeView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('employee-list2')

    def get_context_data(self, **kwargs):
        context = super(CreateEmployeeView, self).get_context_data(**kwargs)
        context['action'] = reverse('employee-new2')

        return context


#Updating of data through this create employee view class.

from django.views.generic import UpdateView


class UpdateEmployeeView(UpdateView):
    model = emp
    template_name = '/HR/add_emp.html'
    form_class = forms.emp_profile
    #this is for login required ..without login u can't go to this page
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateEmployeeView, self).dispatch(*args, **kwargs)


    def get_success_url(self):

        return reverse('employee-list2',)

    def get_context_data(self, **kwargs):
        context = super(UpdateEmployeeView, self).get_context_data(**kwargs)
        context['action'] = reverse('employee-edit2',kwargs={'pk':self.get_object().id})

        return context
#delete data from data base.
from django.views.generic import DeleteView


class DeleteEmployeeView(DeleteView):
    model = emp
    template_name = '/HR/delete_emp.html'


    #this is for login required ..without login u can't go to this page
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteEmployeeView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('employee-list2')


#employee full details.
from django.views.generic import DetailView


class EmployeeView(DetailView):
    model = emp

    template_name = '/HR/emp_profile.html'

    #this is for login required ..without login u can't go to this page
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EmployeeView, self).dispatch(*args, **kwargs)

class CreateEmployeeView1(CreateView):
    model = emp
    template_name = '/HR/candidate_to_emp.html'


    #this is for login required ..without login u can't go to this page
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateEmployeeView1, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('employee-list2')

    def get_context_data(self, **kwargs):
        context = super(CreateEmployeeView1, self).get_context_data(**kwargs)
        context['action'] = reverse('employee-new3')

        return context