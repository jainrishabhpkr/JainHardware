from django.shortcuts import render, redirect
from carts.models import Cart
from orders.models import Order
from products.models import Product
from accounts.forms import LoginForm, GuestForm
from billing.models import BillingProfile
from accounts.models import GuestEmail
# Create your views here.
def home_view(request):
    # del request.session['cart_id']
    cart_obj , new_obj = Cart.objects.new_or_get(request)
    print("home_view runned")
    mydict={'cart':cart_obj}


    # cart_id = request.session.get('cart_id',None)
    # qs = Cart.objects.filter(id = cart_id)
    # if qs.count()==1:
    #     print("cart ID exists")
    #     cart_obj = qs.first()
    #     if request.user.is_authenticated() and cart_obj.user is None:
    #         cart_obj.user = request.user
    #         cart_obj.save()
    # else:
    #     cart_obj = Cart.objects.new(user=request.user)
    #     request.session['cart_id']= cart_obj.id
    #     print("new cart created")
    #     print("sachin")
    #
    #
    # request.session['first_name']='justin'
    return render(request,'carts/home.html',context=mydict)




def cart_update(request):
    print(request.POST)
    print("cart_update runned")

    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id = product_id)
        except Product.DoesNotExist:
            print("product is gone?")
            return redirect("carts:home")
        cart_obj , new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)

        request.session['cart_items'] = cart_obj.products.count()





    # return redirect(product_obj.get_absolute_url())
    return redirect("carts:home")




def checkout_home(request):
    cart_obj , cart_created = Cart.objects.new_or_get(request)
    if cart_created or cart_obj.products.count()==0:
        return redirect("carts:home")
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    user = request.user
    billing_profile = None
    form = LoginForm()
    guest_form = GuestForm()
    guest_email_id = request.session.get('guest_email_id')
    if user.is_authenticated():
        print("rani")
        billing_profile ,billing_profile_created = BillingProfile.objects.get_or_create(user = user , email = user.email)
    elif guest_email_id is  not None:
        print("raja")
        guest_email_obj = GuestEmail.objects.get(id = guest_email_id)
        billing_profile ,billing_guest_profile_created = BillingProfile.objects.get_or_create(email = guest_email_obj.email)
    else:
        pass

    mydict={'object':order_obj, 'billing_profile':billing_profile, 'form':form, 'guest_form':guest_form}

    return render(request,'carts/checkout.html',context=mydict)
