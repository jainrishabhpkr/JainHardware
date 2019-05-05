from django.shortcuts import render
from products.models import Product
# Create your views here.
def searchproductview(request):

    print("raja")
    print(request.GET)
    query = request.GET.get('q', None)
    print(query)
    if query is not None:
        product_list = Product.objects.search(query)
    else:
        product_list = Product.objects.featured()

    mydict={'product_list':product_list,'query':query}
    return render(request,'search/products.html',context=mydict)
