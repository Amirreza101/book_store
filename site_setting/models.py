from django.db import models

from accounts.models import User


# Create your models here.
class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    email = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ایمیل', related_name='contact_email')
    username = models.CharField(blank=True,null=True)
    message = models.TextField(verbose_name='متن تماس با ما')
    created_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    response = models.TextField(verbose_name='متن پاسخ تماس با ما', null=True, blank=True)
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین', default=False)
    is_close = models.BooleanField(default=False, verbose_name='بسته شده/نشده')

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return f"{self.email} - {self.title}"
