from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse

from product.models import Product
 
# Create your views here.



def index_view(request:HttpRequest):
    products=Product.objects.all()
    
    return render(request,"main/index.html",{"products":products})
    
   


