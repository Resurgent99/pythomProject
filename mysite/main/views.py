from django.shortcuts import render
from .models import View, Yrok2, Product2
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Sum, Count


def index(request):
    return render(request, 'main/index.html')

def product(request):
    return render(request, 'main/product.html')

def django_product(request):
    return render(request, 'main/django_product.html')

def HTML_product(request):
    return render(request, 'main/HTML_product.html')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_context_data(title= 'Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

#Задание 2(1,2)
def spiski(request):
    spisok = Yrok2.objects.all()
    queryset = Yrok2.objects.all().annotate(count = Count('name'))
    queryset1 = Yrok2.objects.aggregate(Sum('view'))
    total = 0
    for i in queryset:
        total +=1

    return render(request, 'main/spisok.html', {'yrok': spisok, 'queryset1': queryset1, 'total': total})


