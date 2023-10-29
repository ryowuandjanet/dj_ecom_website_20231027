from datetime import datetime
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import get_object_or_404,redirect
from .carts import Cart
from product.models import Product
from .models import Coupon

class AddToCart(generic.View):
    def post(self, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get('product_id'))
        cart = Cart(self.request)
        cart.update(product.id,1)
        return redirect('cart')

class CartItems(generic.TemplateView):
    template_name = 'cart/cart.html'

    def get(self, request, *args, **kwargs):
        product_id = request.GET.get('product_id', None)
        quantity = request.GET.get('quantity',None)
        clear = request.GET.get('clear',False)
        cart = Cart(request)
        print(cart.coupon,"coupon")

        if product_id and quantity:
            product = get_object_or_404(Product,id=product_id)
            if int(quantity) > 0:
                if product.in_stock:
                    cart.update(int(product_id),int(quantity))
                    return redirect('cart')
                else:
                    messages.warning(request, "Your account expires in three days.")
                    return redirect('cart')
            else:
                cart.update(int(product_id),int(quantity))
                return redirect('cart')
        
        if clear:
            cart.clear()
            return redirect('cart')
        
        return super().get(request, *args, **kwargs)

class AddCoupon(generic.View):
    def post(self, *args, **kwargs):
        code = self.request.POST.get('coupon','')
        coupon = Coupon.objects.filter(code__iexact=code,active=True)
        cart = Cart(self.request)

        if coupon.exists():
            coupon = coupon.first()
            current_date=datetime.date(timezone.now())
            active_date = coupon.activate_date
            expiry_date = coupon.expiry_date

            if current_date > expiry_date:
                messages.warning(self.request, "The coupon expired")
                return redirect('cart')
            
            if current_date > active_date:
                messages.warning(self.request, "The coupon is yet to be available")
                return redirect('cart')
            
            cart.add_coupon(coupon.id)
            messages.warning(self.request,"Your coupon has ben include successfully")
            return redirect('cart')
        else:
            messages.warning(self.request,"Invalid coupon code")
            return redirect('cart')