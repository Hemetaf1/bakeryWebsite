from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import CustomUser, Bakery
from .models import Order


class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email")  # به همراه password1 و password2 از UserCreationForm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class BakerySignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name  = forms.CharField(required=True, max_length=100, label="نام قنادی")
    phone = forms.CharField(required=False, max_length=20, label="تلفن")
    address = forms.CharField(required=False, max_length=255, label="آدرس")

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email")  # به همراه password1 و password2

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_bakery = True
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        # پس از ذخیره کاربر، یک رکورد Bakery مرتبط با آن ایجاد می‌کنیم:
        bakery = Bakery.objects.create(
            user=user,
            name=self.cleaned_data['name'],
            phone=self.cleaned_data.get('phone', ''),
            address=self.cleaned_data.get('address', '')
        )
        return user


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('bakery', 'description')  # مشتری را از روی request.user تعیین می‌کنیم، status هم پیش‌فرض است.
