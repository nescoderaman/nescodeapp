
# Create your views here.

from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.template import RequestContext



@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']

            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'registration/register.html',
    variables,
    )

def register_success(request):
    return render_to_response(

    'registration/success.html',
    )
from django.contrib import messages
def logout_page(request):
    logout(request)
    messages.info(request, 'You have successfully logged out. Come back soon.')
    return HttpResponseRedirect('/')


@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )



def index(request):
    return render_to_response(
    'index.html',
    { 'user': request.user }
    )


def success_password(request):
    return render_to_response('registration/update_success.html',)



from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm

def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='password_reset_confirm.html',
        uidb64=uidb64, token=token, post_reset_redirect=reverse('password_reset_complete'))


def reset(request):
    return password_reset(request, template_name='forgetpass.html',
        email_template_name='password_reset_email.html',
        post_reset_redirect=reverse('success'))


def password_reset_complete(request):
    return render_to_response(
    'password_reset_complete.html',
    { 'user': request.user }
    )