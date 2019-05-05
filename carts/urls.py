from django.conf.urls import url,include

from . import views
urlpatterns = [
    url(r'^home', views.home_view, name ='home'),
    url(r'^update', views.cart_update, name ='update'),
    url(r'^checkout', views.checkout_home, name ='checkout'),


]
