"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views as main_views
from django.contrib.auth import views as auth_views
from main import views  # import the view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.mainPage, name='mainPage'),  # صفحه اصلی
    path('register/customer/', main_views.register_customer, name='register_customer'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('dashboard/', main_views.dashboard, name='dashboard'),
    path('order/new/', main_views.create_order, name='create_order'),
    path('customize/', views.customize, name='customize'),
    path('registerBakery/', views.register_bakery, name='registerBakery'),

]


