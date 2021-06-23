"""courier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from products.views import CategoryView
from products.views import ProductView
from user.views import CourierRegisterView, ProfileRegisterView, ProfileLoginView
from orders.views import OrderView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/register', ProfileRegisterView.as_view()),
    path('profile/login', ProfileLoginView.as_view()),
    path('courier/register', CourierRegisterView.as_view()),
    path('category/create', CategoryView.as_view({'post':'create'})),
    path('product/create', ProductView.as_view({'post': 'create'})),
    path('category', CategoryView.as_view({'get':'list'})),
    path('product', ProductView.as_view({'get':'list'})),
    path('product/<int:pk>', ProductView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('category/<int:pk>', CategoryView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('order', OrderView.as_view({'get':'list'})),
    path('order/create', OrderView.as_view({'post':'create'}))
]
