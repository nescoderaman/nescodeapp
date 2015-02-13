from __future__ import print_function
from cms.sitemaps import CMSSitemap
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

from django.conf.urls import patterns, include, url
from login.views import *
import login.views
import offer_letter.views
import offer_letter.emp_view




admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                       url(r'^list/$', offer_letter.views.ListContactView.as_view(),name='employee-list', ),
                       url(r'^new/$', offer_letter.views.CreateEmployeeView.as_view(),
                           name='employee-new', ),
                       url(r'^edit/(?P<pk>\d+)/$', offer_letter.views.UpdateEmployeeView.as_view(),
                           name='employee-edit', ),
                       url(r'^delete/(?P<pk>\d+)/$', offer_letter.views.DeleteEmployeeView.as_view(),
                           name='employee-delete', ),
                       url(r'^employee_details/(?P<pk>\d+)/$', offer_letter.views.EmployeeView.as_view(),name='employee-view', ),
                       url(r"^(?P<pk>\d+)/offer_letter/$", offer_letter.views.offerletter.as_view(), name='get-offer',),
                            # Below is login module url like registration login logout etc.
                       #url(r'^$', index),
                       url(r'^login/$', 'django.contrib.auth.views.login',name='login'),
                       url(r'^logout/$', logout_page),
                            # If user is not login it will redirect to login page
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
                       url(r'^register/$', register),
                       url(r'^register/success/$', register_success),
                       url(r'^home/$', offer_letter.views.home,name='home'),
                            #password reset and email authentication url
                       url(r'^success/$','login.views.success_password',name="success"),
                       url(r'^update-password/$', 'login.views.reset', name='reset'),
                       url(r'^account/', include('django.contrib.auth.urls')),

                       #url(r'^reset/$', 'login.views.reset', name='reset'),
                       url(r'^password/reset/confirm/complete/$',
                                   login.views.password_reset_complete,
                                   name='password_reset_complete'), # must be named for reverse to work
                       url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                            'login.views.reset_confirm',
                            name='password_reset_confirm'),

                      #HR Module
                      url(r'human-resource/$',offer_letter.views.hr_module.as_view(),name='hr_module', ),
                      url(r'create-employee/$',offer_letter.views.register_candidate,name='register', ),
                      url(r'create-employee/success/$',offer_letter.views.employee_success,name='empployee_success', ),
                      url(r'^profile/$', 'offer_letter.emp_view.profile', name='profile'),

                      url(r'^edit1111/(?P<pk>\d+)/$', offer_letter.emp_view.UpdateEmployeeView.as_view(),
                           name='employee-edit1', ),
        ) + staticfiles_urlpatterns() + urlpatterns  # NOQA
