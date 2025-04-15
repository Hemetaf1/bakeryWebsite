from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Bakery, Order

# ثبت مدل CustomUser با استفاده از UserAdmin پیش‌فرض Django برای نمایش مناسب در ادمین
class CustomUserAdmin(UserAdmin):
    # نمایش فیلدهای اضافه در صفحه لیست کاربران (اختیاری)
    list_display = ('username', 'email', 'is_customer', 'is_bakery', 'is_staff')
    list_filter = ('is_customer', 'is_bakery', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Bakery)
admin.site.register(Order)
