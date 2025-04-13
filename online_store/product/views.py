from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from.models import Product
from django.contrib import messages

# Create your views here.

def add_product_view(request:HttpRequest):
    if not request.user.is_staff:
        messages.success(request, "only staff can add prodect", "alert-warning")
        return redirect("main:home_view")
    if request.method=="POST":
        prodect=Product(title=request.POST["title"], content=request.POST["content"],types=request.POST["types"], price=request.POST["price"], product_image=request.FILES["product_image"] )
        prodect.save() 
        
        return redirect('product:all_product_view')
    
    return render(request,"product/add_product.html")


def all_product_view(request:HttpRequest):
    products=Product.objects.all()
    
    return render(request,"product/all_product.html",{"products":products})

def detail_product_view(request:HttpRequest, product_id:int):
    product=Product.objects.get(pk=product_id)
    
    return render(request,"product/detail_product.html",{"product":product})



def update_product_view(request: HttpRequest , product_id:int):
    if not request.user.is_staff:
        messages.success(request, "only staff can updat prodect", "alert-warning")
        return redirect("main:home_view")
    
    product=Product.objects.get(pk=product_id)
    
    if request.method=="POST":
        product.title=request.POST["title"] 
        product.content=request.POST["content"] 
        product.types=request.POST["types"]
        product.price=request.POST["price"]
        if "product_image" in request.FILES: product.product_image=request.FILES["product_image"] 
        product.save()
        
        return redirect('product:detail_product_view',product_id=product.id)
    
    return render(request,"product/update_product.html",{"product":product})


def delete_product_view(request: HttpRequest , product_id:int):
    if not request.user.is_staff:
        messages.success(request, "only staff can delete prodect", "alert-warning")
        return redirect("main:home_view")
    
    product=Product.objects.get(pk=product_id)
    product.delete()
    
    return redirect('product:all_product_view')




def search_product_view(request: HttpRequest):
    # products=Product.objects.all()

    if "product_type" in request.GET and request.GET["product_type"]=="All":
        products=Product.objects.all()

        print('it is all')
    elif "product_type" in request.GET:
        products=Product.objects.filter(types=request.GET["product_type"])

        
    search_query = request.GET.get("search", "")

    if search_query:
        products = products.filter(title__icontains=search_query)
        
        
    return render(request,"product/search_product.html",{"products":products}) 



def Perfumes_product_view(request:HttpRequest):
    products=Product.objects.filter(types="Perfumes")
    return render(request,"product/Perfumes_product.html",{"products":products})


def Oud_product_view(request:HttpRequest):
    products=Product.objects.filter(types="Oud")
    return render(request,"product/Oud_product.html",{"products":products})

def Other_product_view(request:HttpRequest):
    products=Product.objects.filter(types="Other")
    return render(request,"product/Other_product.html",{"products":products})


def cart_view(request:HttpRequest, product_id:int):
    product=Product.objects.get(pk=product_id)
    
    return render(request,"product/cart.html",{"product":product})

