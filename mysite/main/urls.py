from django.urls import path
from . import views
from .views import spiski



urlpatterns = [
    path('', views.index, name='home'),
    path('python', views.product, name='product'),
    path('django', views.django_product, name='django'),
    path('html', views.HTML_product, name='html'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('spisok', views.spiski, name='spiski'),
]






