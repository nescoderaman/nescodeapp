from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from easy_pdf.views import PDFTemplateView
from offer_letter import forms
from offer_letter.models import offer1


class ListContactView(ListView):
    model = offer1
    template_name = 'employee_list.html'

    #this is for login required ..without login u can't go to this page
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ListContactView, self).dispatch(*args, **kwargs)


from django.core.urlresolvers import reverse
from django.views.generic import CreateView

#inserting of data through this create employee view class.

class CreateEmployeeView(CreateView):
    model = offer1
    template_name = 'edit_employee.html'

    form_class = forms.EmployeeForm
    #this is for login required ..without login u can't go to this page
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateEmployeeView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('employee-list')

    def get_context_data(self, **kwargs):
        context = super(CreateEmployeeView, self).get_context_data(**kwargs)
        context['action'] = reverse('employee-new')

        return context


#Updating of data through this create employee view class.

from django.views.generic import UpdateView


class UpdateEmployeeView(UpdateView):
    model = offer1
    template_name = 'edit_employee.html'
    form_class = forms.EmployeeForm
    #this is for login required ..without login u can't go to this page
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateEmployeeView, self).dispatch(*args, **kwargs)


    def get_success_url(self):

        return reverse('employee-list',)

    def get_context_data(self, **kwargs):
        context = super(UpdateEmployeeView, self).get_context_data(**kwargs)
        context['action'] = reverse('employee-edit',kwargs={'pk':self.get_object().id})

        return context
#delete data from data base.
from django.views.generic import DeleteView


class DeleteEmployeeView(DeleteView):
    model = offer1
    template_name = 'delete_employee.html'


    #this is for login required ..without login u can't go to this page
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteEmployeeView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('hr_module')


#employee full details.
from django.views.generic import DetailView


class EmployeeView(DetailView):
    model = offer1

    template_name = 'employee_profile.html'

    #this is for login required ..without login u can't go to this page
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EmployeeView, self).dispatch(*args, **kwargs)



#pdf generation using easy pdf.
class offerletter(PDFTemplateView):
    model = offer1
    template_name = "employee.html"


    #this is for login required ..without login u can't go to this page
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(offerletter, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(offerletter, self).get_context_data(
            pagesize="A4",
            title="Offer Letter",


            **kwargs)

        if 'pk' in self.kwargs:
            context['tool'] = offer1.objects.get(id=self.kwargs['pk'])

            return context
        def get_success_url(self):
            return reverse('get-pdf')

class hr_module(ListView):
    model = offer1
    template_name = 'HR/hr_module.html'

    #this is for login required ..without login u can't go to this page
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(hr_module, self).dispatch(*args, **kwargs)

