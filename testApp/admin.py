from django.contrib import admin
from testApp.models import Product,Cart,Order

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	list_display=['id','item_name','item_detail','item_price','item_image']
class CartAdmin(admin.ModelAdmin):
	#list_display=["cart"]
	pass

class OrderAdmin(admin.ModelAdmin):
	#list_display=["order"]
	pass


admin.site.register(Product,ProductAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(Order,OrderAdmin)
