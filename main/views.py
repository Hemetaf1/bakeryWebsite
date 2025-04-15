from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomerSignUpForm, BakerySignUpForm
from .forms import OrderForm
from .models import Order
from django.http import HttpResponse

from django.shortcuts import render

def mainPage(request):
    return render(request, 'mainPage.html')


def register_customer(request):
    if request.method == "POST":
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # هدایت به داشبورد یا صفحه اصلی پس از ثبت‌نام موفق
    else:
        form = CustomerSignUpForm()
    return render(request, 'register_customer.html', {'form': form})

def register_bakery(request):
    if request.method == "POST":
        form = BakerySignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # هدایت به داشبورد قنادی
    else:
        form = BakerySignUpForm()
    return render(request, 'registerBakery.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    user = request.user
    context = {}
    if user.is_bakery:
        # کاربر قنادی: نمایش سفارش‌هایی که برای این قنادی ثبت شده
        bakery = getattr(user, 'bakery_profile', None)  # شیء Bakery مرتبط با کاربر
        if bakery:
            orders = Order.objects.filter(bakery=bakery)
        else:
            orders = []
        context['bakery'] = bakery
        context['orders'] = orders
    elif user.is_customer:
        # کاربر مشتری: نمایش سفارش‌هایی که خودش ثبت کرده
        orders = Order.objects.filter(customer=user)
        context['orders'] = orders
    return render(request, 'dashboard.html', context)


@login_required
def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user    # تنظیم مشتری سفارش به کاربر جاری
            order.status = 'pending'         # وضعیت اولیه
            order.save()
            # پیام موفقیت و هدایت (مثلاً به داشبورد یا صفحه سفارشات)
            return redirect('dashboard')
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})


from django.shortcuts import render

def customize(request):
    return render(request, 'customize.html')
