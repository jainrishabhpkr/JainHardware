from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from carts.models import Cart

from products.models import Product

# Create your views here.


# class ProductListView(ListView):
#     model=Product
#     template_name='products/products.html'

def listview(request):
    product_list = Product.objects.all()
    print("bat")
    mydict={'product_list':product_list,"bat":"britannia"}
    return render(request,'products/products.html',context=mydict)

# class ProductDetailView(DetailView):
#     model=Product
#     template_name='products/product.html'

def productview(request, slug):
    print(slug)

    product = get_object_or_404(Product, slug = slug)

    print('appple')
    cart_obj , new_obj = Cart.objects.new_or_get(request)
    mydict={'product':product, 'cart':cart_obj}
    return render(request,'products/product.html',context=mydict)

def featuredlistview(request):
    product_list = Product.objects.featured()
    print("bat")
    mydict={'product_list':product_list,"bat":"britannia"}
    return render(request,'products/featuredproducts.html',context=mydict)

def featuredproductview(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    print('appple')
    mydict={'product':product}
    return render(request,'products/featuredproduct.html',context=mydict)
