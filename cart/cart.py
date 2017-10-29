from decimal import Decimal
from django.conf import settings
from main.models import Product

class Cart(object):

    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False,size=10.0):
        product__id = str(product.pk)
        strsize = str(int(size*10 + 1000))
        p = product__id+strsize
        # print(product.pic1)
        # ppp = "%s-%s"%(product__id,strsize)
        if p not in self.cart:
            self.cart[p] = {'quantity': 0,
                            'name' : product.product_Name,
                            'price': str(product.unit_Price),
                            'size' : str(size),
                            'pk' : product__id,
                            'p' : p,
#                            'pic' : str(product.pic1),
                            'description': str(product.product_Description),}
        self.cart[p]['quantity'] += 1
        self.save()

    def sub(self, product, quantity=1, update_quantity=False,size=10.0):
        product__id = str(product.pk)
        strsize = str(int(size*10 + 1000))
        p = product__id+strsize
        # print(product.pic1)
        # ppp = "%s-%s"%(product__id,strsize)
        if p not in self.cart:
            self.cart[p] = {'quantity': 0,
                            'name' : product.product_Name,
                            'price': str(product.unit_Price),
                            'size' : str(size),
                            'pk' : product__id,
                            'p' : p,
#                            'pic' : str(product.pic1),
                            'description': str(product.product_Description),}
        if self.cart[p]['quantity'] > 1:
            self.cart[p]['quantity'] -= 1
        self.save()


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self,product_p):
        # product_id = str(product.id)
        if product_p in self.cart:
            del self.cart[product_p]
        self.save()

    def __iter__(self):

        product_ids = self.cart.keys()
        products = Product.objects.filter(pk__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
