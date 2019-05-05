from django.conf.urls import url,include

from . import views
urlpatterns = [
    url(r'^products/', views.listview, name ='products'),
    url(r'^(?P<slug>[-\w]+)/$', views.productview ,name = 'product'),
    url(r'^featuredproducts/$', views.featuredlistview ,name = 'featuredproducts'),
    url(r'^featuredproducts/(?P<product_id>\d+)/$', views.featuredproductview ,name = 'featuredproduct'),

]
