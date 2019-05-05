from django.db import models
from django.db.models.signals import pre_save, post_save
from carts.models import Cart
from ecommerce.utils import unique_order_id_generator
# Create your models here.
ORDER_STATUS_CHOICES = (
('created','Created'),
('paid','Paid'),
('shipped','Shipped'),
('refunded','refunded')
)
class Order(models.Model):
    order_id = models.CharField(max_length=120, blank = True)
    cart = models.ForeignKey(Cart)
    status   = models.CharField(max_length=120 ,default='created', choices = ORDER_STATUS_CHOICES)
    shippingtotal = models.DecimalField(default=30.25 , max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0 , max_digits=100, decimal_places=2)

    def __str__(self):
        return self.order_id

    def update_total(self):
        cart_total = self.cart.total
        shippingtotal = self.shippingtotal
        new_total = float(cart_total) + float(shippingtotal) #taxes add karna hhai to
        self.total = new_total
        self.save()
        return new_total



def pre_save_order_receiver(sender, instance, *args , **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)

pre_save.connect(pre_save_order_receiver, sender=Order)

def post_save_cart_total(sender, instance,created, *args , **kwargs):
    print("tony")
    if not created:
        cart_obj = instance
        cart_id = cart_obj.id
        cart_total = cart_obj.total
        qs= Order.objects.filter(cart__id = cart_id)
        if qs.count()==1:

            order_obj = qs.first()
            print(order_obj)
            print("chotu")
            order_obj.update_total()
            print("tanu")


post_save.connect(post_save_cart_total, sender=Cart)

def post_save_order(sender, instance, created, *rags, **kwargs):
    print("runnnig")
    if created:
        print("updating")
        instance.update_total()

post_save.connect(post_save_order, sender=Order)
