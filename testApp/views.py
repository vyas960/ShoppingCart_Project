from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from testApp.models import Product,Cart,Order
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
# import pdb;pdb.set_trace()
# Create your views here.

def home_view(request):
	product=Product.objects.all()
	return render(request,'testApp/home.html',{'product':product})

@login_required
def addToCart_view(request,pk):
	cart=Cart.objects.filter(user=request.user)
	if cart:
		cart.delete()
	product=Product.objects.get(pk=pk)
	cart=Cart.objects.get_or_create(product=product,user=request.user)
	return HttpResponseRedirect(reverse('cart'))
	# return redirect("/cart")

@login_required
def cart_view(request):
	if request.method=='POST':
		cart_id = request.POST.getlist('cart_id')
		quantity = request.POST.getlist('quantity')
		amount = request.POST.getlist('amount')
		grand_total = request.POST.get('grandTotal')
		for i in range(len(cart_id)):
			cart = Cart.objects.get(id=cart_id[i])
			cart.quantity = quantity[i]
			cart.amount = amount[i]
			cart.save()
		cart=Cart.objects.filter(user=request.user)
		return render(request,'testApp/order.html',{'cart':cart,'grand_total':grand_total})
	else:
		cart=Cart.objects.filter(user=request.user)
		return render(request,'testApp/cart.html',{'cart':cart})

@login_required
def removeToCart_view(request,pk):
	cart=Cart.objects.get(pk=pk)
	cart.delete()
	return redirect('/cart')

@login_required
def order_View(request):
	if request.method=='POST':
		grand_total = request.POST.get('grandTotal')
		cart=Cart.objects.filter(user=request.user)
		for carts in cart:
			obj_id = carts.product
			quantity=carts.quantity
			amount=carts.amount
		order=Order.objects.create(product=obj_id,grandTotal=grand_total,user=request.user,quantity=quantity,amount=amount)
		cart.delete()
		return redirect('/order')
	else:
		order=Order.objects.filter(user=request.user)
		return render(request,'testApp/confirm_order.html',{'order':order})
