from django.contrib import admin
from products.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','price','featured','slug')
    prepopulated_fields={'slug':('title',)}
    list_display_links=('id','title')
    list_editable = ('featured',)
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
