from .models import *
import json 


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    items = []
    order = {'get_cart_total':0,'count':0}
    for i in cart:
        try:
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]["quantity"])
            order['get_cart_total'] += total

            order_item = {
                'product':{
                    'id':product.id,
                    'title':product.title,
                    'price':product.price,
                    'thumbnail_1':product.thumbnail_1
                },
                'quantity':cart[i]['quantity'],
                'get_total':total
            }
            items.append(order_item)
        except:
            pass
    return {'items':items,'order':order}