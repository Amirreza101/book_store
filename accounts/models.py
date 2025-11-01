from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=12, blank=True, null=True, verbose_name='شماره همراه')
    avatar = models.ImageField(upload_to='image/avatar/',null= True,blank=True,verbose_name='تصویر آواتار')
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.email


