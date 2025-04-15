from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # نقش‌های ممکن برای کاربر
    is_customer = models.BooleanField(default=False, verbose_name="مشتری")
    is_bakery   = models.BooleanField(default=False, verbose_name="قنادی")
    # می‌توانید فیلدهای اضافی هم در صورت نیاز اضافه کنید (مثلاً شماره تماس)
    # اما برای MVP تنها از این بولین‌ها برای تشخیص نوع کاربر استفاده می‌کنیم.


class Bakery(models.Model):
    user       = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='bakery_profile')
    name       = models.CharField(max_length=100, verbose_name="نام قنادی")
    address    = models.CharField(max_length=255, verbose_name="آدرس", null=True, blank=True)
    phone      = models.CharField(max_length=20, verbose_name="تلفن", null=True, blank=True)
    # می‌توان فیلدهای دیگری مانند مجوز کسب، توضیحات، تصویر و ... نیز افزود
    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders', verbose_name="مشتری")
    bakery   = models.ForeignKey(Bakery, on_delete=models.CASCADE, related_name='orders', verbose_name="قنادی")
    description = models.TextField(verbose_name="جزئیات سفارش", blank=True)
    status   = models.CharField(max_length=20, choices=[('pending', 'در انتظار'), 
                                                        ('processing', 'در حال انجام'), 
                                                        ('done', 'انجام‌شده')], 
                                 default='pending', verbose_name="وضعیت")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")

    def __str__(self):
        return f"سفارش {self.id} - {self.customer.username} برای {self.bakery.name}"
