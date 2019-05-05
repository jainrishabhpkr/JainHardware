from django.conf.urls import url,include

from . import views
urlpatterns = [
    url(r'^products/', views.searchproductview, name ='searchproducts'),

]
