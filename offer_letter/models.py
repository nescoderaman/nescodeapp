from audioop import reverse
from django.db import models

#this model is for candidate profile.
class offer1(models.Model):
    salutation = models.CharField(max_length=4,
                                  choices=(('Mr', 'Mr'),
                                           ('Mrs', 'Mrs'),),blank=True,null=True,default='Select')
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


#below model for employee  details (Employee profile)
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):

    user = models.OneToOneField(User)
    dob = models.CharField(max_length=100,blank=True, null=True,default='NA')
    presnal_email = models.CharField(max_length=100,blank=True, null=True,default='NA')
    mobile = models.CharField(max_length=100,blank=True, null=True,default='NA')
    phone = models.CharField(max_length=100,blank=True, null=True,default='NA')
    alternet_no = models.CharField(max_length=100,blank=True, null=True,default='NA')
    company = models.CharField(max_length=100,blank=True, null=True,default='NA')
    doj = models.CharField(max_length=100,blank=True, null=True,default='NA')
    department = models.CharField(max_length=100,blank=True, null=True,default='NA')
    designation = models.CharField(max_length=100,blank=True, null=True,default='NA')
    home_address = models.CharField(max_length=100,blank=True, null=True,default='NA')
    local_address = models.CharField(max_length=100,blank=True, null=True,default='NA')
    ctc = models.CharField(max_length=100,blank=True, null=True,default='NA')
    total_leave = models.CharField(max_length=100,blank=True, null=True,default='NA')
    total_exp = models.CharField(max_length=100,blank=True, null=True,default='NA')
    employment_type = models.CharField(max_length=100,blank=True, null=True,default='NA')
    job_location  = models.CharField(max_length=100,blank=True, null=True,default='NA')
    Passport_Number = models.CharField(max_length=100,blank=True, null=True,default='NA')
    Date_of_Issue = models.CharField(max_length=100,blank=True, null=True,default='NA')
    Place_of_Issue = models.CharField(max_length=100,blank=True, null=True,default='NA')
    Marital_Status = models.CharField(max_length=100,blank=True, null=True,default='NA')
    Blood_Group = models.CharField(max_length=100,blank=True, null=True,default='NA')
    Relation = models.CharField(max_length=100,blank=True, null=True,default='NA')
    PAN_Number = models.CharField(max_length=100,blank=True, null=True,default='NA')
    Salary_Mode = models.CharField(max_length=100,blank=True, null=True,default='NA')
    Bank_Name = models.CharField(max_length=100,blank=True, null=True,default='NA')
    Bank_AC_No = models.CharField(max_length=100,blank=True, null=True,default='NA')
    def __str__(self):
          return "%s's profile" % self.user


    def get_absolute_url(self):
        return reverse('employee-view1', kwargs={'pk': self.id})



def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)



#for employee who is not system user
class emp(models.Model):
    offer1 = models.ForeignKey(offer1)
    dob = models.CharField(max_length=100,blank=True, null=True,default='NA')
    presnal_email = models.CharField(max_length=100,blank=True, null=True,default='NA')
    mobile = models.CharField(max_length=100,blank=True, null=True,default='NA')
    phone = models.CharField(max_length=100,blank=True, null=True,default='NA')
    alternet_no = models.CharField(max_length=100,blank=True, null=True,default='NA')
    company = models.CharField(max_length=100,blank=True, null=True,default='NA')
    doj = models.CharField(max_length=100,blank=True, null=True,default='NA')
    department = models.CharField(max_length=100,blank=True, null=True,default='NA')
    designation = models.CharField(max_length=100,blank=True, null=True,default='NA')
    home_address = models.CharField(max_length=100,blank=True, null=True,default='NA')
    local_address = models.CharField(max_length=100,blank=True, null=True,default='NA')
    ctc = models.CharField(max_length=100,blank=True, null=True,default='NA')
    total_leave = models.CharField(max_length=100,blank=True, null=True,default='NA')
    total_exp = models.CharField(max_length=100,blank=True, null=True,default='NA')
    employment_type = models.CharField(max_length=100,blank=True, null=True,default='NA')
    job_location  = models.CharField(max_length=100,blank=True, null=True,default='NA')
    Passport_Number = models.CharField(max_length=100,blank=True, null=True,default='NA')
    Date_of_Issue = models.CharField(max_length=100,blank=True, null=True,default='NA')
    Place_of_Issue = models.CharField(max_length=100,blank=True, null=True,default='NA')
    Marital_Status = models.CharField(max_length=100,blank=True, null=True,default='NA')
    Blood_Group = models.CharField(max_length=100,blank=True, null=True,default='NA')
    Relation = models.CharField(max_length=100,blank=True, null=True,default='NA')
    PAN_Number = models.CharField(max_length=100,blank=True, null=True,default='NA')
    Salary_Mode = models.CharField(max_length=100,blank=True, null=True,default='NA')
    Bank_Name = models.CharField(max_length=100,blank=True, null=True,default='NA')
    Bank_AC_No = models.CharField(max_length=100,blank=True, null=True,default='NA')
    def __str__(self):
        return self.offer1

    def get_absolute_url(self):
        return reverse('employee-view2', kwargs={'pk': self.id})

