from audioop import reverse
from django.contrib.admin.widgets import AdminDateWidget
from django.core.files.storage import FileSystemStorage
from django.db import models


class offer1(models.Model):
    salutation = models.CharField(max_length=4,
                                  choices=(('Mr', 'Mr'),
                                           ('Mrs', 'Mrs'),))
    name = models.CharField(max_length=100)
    empid = models.CharField(max_length=100)
    doj = models.CharField(max_length=255,blank=True,null=True)
    designation = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    supervisername = models.CharField(max_length=100)
    ctc = models.CharField(max_length=100)
    location = models.CharField(max_length=50,
                                choices=(('Bangalore', 'Bangalore'),
                                         ('New Delhi', 'New Delhi'),))
    traning_duration = models.CharField(max_length=100)
    leave = models.CharField(max_length=100)
    add1 = models.CharField(max_length=200)
    add2 = models.CharField(max_length=200)
    add3 = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('employee-view', kwargs={'pk': self.id})


# for profile picture,
from django.db import models


class ProfileImage(models.Model):
    image = models.FileField(upload_to='profile/%Y/%m/%d')

    def __unicode__(self):

        return self.image


