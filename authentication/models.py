from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from .managers import UserManager

class School(models.Model):
    name = models.CharField(max_length=225)


    def __str__(self):
        return self.name



class User(AbstractBaseUser, PermissionsMixin):
    ACTION_PREFERENCE = (
        ('1', 'No preference'),
        ('2', 'Own a room/Need room mate'),
        ('3', 'Need a room/Need room mate'),
    )

    SEX = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Prefer not to specify', 'Prefer not to specify'),
    )
    
    
    SOCIALIZE = (
        ('1', 'Introvert'),
        ('2', 'Ambivert'),
        ('3', 'Extrovert'),
    )

    
    GENDER = (
        ('1', 'Male'),
        ('2', 'Strictly Female'),
        ('3', 'Any'),
    )
    PET = (
        ('1', 'Pets are not allowed'),
        ('2', 'Sure, you can bring yours'),
    )
    SMOKING = (
        ('1', 'Not allowed'),
        ('2', 'Allowed'),
    )

    AGE_RANGE = (
        ('1', '< 18'),
        ('2', '18 - 25'),
        ('3', '> 25'),
    )
    RELIGION = (
        ('1', 'Christian'),
        ('2', 'Moslem'),
        ('3', 'I am ok with any..'),
    )
    CLEAN = (
        ('1', 'We hire cleaners'),
        ('2', 'We do the cleaning ourselves'),
    )

 
    NOISE = (
        ('1', 'If it is not really loud, No problem'),
        ('2', 'If anyone needs silence, that is the law of the house'),
        ('3', 'Frequent quiet time'),
    )
    TOWNERS = (
        ('1', 'Not allowed'),
        ('2', 'Allowed'),
    )
    FAMILY = (
        ('1', 'Not allowed'),
        ('2', 'Allowed'),
    )


 
    
 




    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30)
    avatar = models.ImageField(upload_to='users/', null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=True)
    email_verified = models.BooleanField(_('email verified'), default=True)
    action = models.CharField(max_length=14, null=True, default='1', choices=ACTION_PREFERENCE)
    sex = models.CharField(max_length=225, null=True, choices=SEX)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, blank=True, null=True)
    
    pref_room_gender = models.CharField(max_length=14, null=True, choices=GENDER)
    pets_allowed = models.CharField(max_length=14, null=True, choices=PET)
    smoking_allowed = models.CharField(max_length=14, null=True, choices=SMOKING)
    pref_age_range = models.CharField(max_length=14, null=True, choices=AGE_RANGE)
    pref_religion = models.CharField(max_length=14, null=True, choices=RELIGION)
    room_clean = models.CharField(max_length=14, null=True, choices=CLEAN)
    room_noise = models.CharField(max_length=14, null=True, choices=NOISE)
    out_of_towners = models.CharField(max_length=14, null=True, choices=TOWNERS)
    family_visits = models.CharField(max_length=14, null=True, choices=FAMILY)
    course_of_interest = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=225, blank=True)
    phone_no = models.CharField(max_length=14, blank=True)
    
  
   
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('username')
        verbose_name_plural = _('users')


    
    @property
    def avatarUrl(self):
        try:
            url = self.avatar.url
        except:
            url = ''
        return url

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)




