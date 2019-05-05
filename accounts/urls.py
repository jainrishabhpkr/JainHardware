from django.conf.urls import url,include

from . import views
urlpatterns = [
    url(r'^login', views.login_page, name ='login'),
    url(r'^register', views.register_page, name ='register'),
    url(r'^guest', views.guest_register_view, name ='guest_register'),
    url(r'^logout', views.logout_view, name ='logout'),


]
