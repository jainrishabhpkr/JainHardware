"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from home import views
# from products import views as v1
# from search import views as v2
# from carts import views as v3

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',views.homeview ,name='home'),
    url(r'^contact/',views.contactview ,name='contact'),
    # url(r'^login/',views.login_page ,name='login'),
    # url(r'^register/',views.register_page,name='register'),
    # url(r'^homecarts/',v3.home_view,name='cartshome'),
    url(r'^products/', include('products.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^cart/', include('carts.urls', namespace='carts')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    # url(r'^products/',v1.ProductListView.as_view(),name='products'),
    # url(r'^products-fbv/',v1.listview,),
    # url(r'^products/(?P<product_id>\d+)/$',v1.ProductDetailView.as_view(),name='product'),
    # url(r'^products-fbv/(?P<pk>\d+)/',v1.productview)
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
