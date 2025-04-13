from django.urls import path
from . import views
app_name="product"

urlpatterns = [
    
    path("add/",views.add_product_view,name="add_product_view"),
    path("all/",views.all_product_view,name="all_product_view"),
    path('detail/<int:product_id>/', views.detail_product_view, name='detail_product_view'),
    path('update/<int:product_id>/', views.update_product_view, name='update_product_view'),
    path('delete/<int:product_id>/', views.delete_product_view ,name='delete_product_view'),
    path('search/', views.search_product_view, name="search_product_view"),
    path('Perfumes/', views.Perfumes_product_view , name="Perfumes_product_view"),
    path('Oud/', views.Oud_product_view , name="Oud_product_view"),
    path('Other/', views.Other_product_view , name="Other_product_view"),
    path("cart/<product_id>", views.cart_view,name="cart_view")
    
    
    
]
