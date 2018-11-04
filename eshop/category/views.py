from django.shortcuts import render
from django.http import HttpResponse
from .models import Laptop
# Create your views here.


def test(request):
    laptop_instance = Laptop()
    all_laptop = laptop_instance.get_all()
    ctx = {}
    ctx['category_name'] = 'all'
    ctx['all_laptop'] = all_laptop
    return render(request , 'category/index.html' , ctx)
    # return HttpResponse('asdasd')


def laptops_view(request):
    ctx = {}
    all_laptops = Laptop.objects.all()
    ctx['all_laptops'] = all_laptops
    ctx['category_name'] = 'laptops'
    for elem in all_laptops:
        print(elem.image)
    # print(all_laptops)
    return render(request , 'category/laptops.html' , ctx)
