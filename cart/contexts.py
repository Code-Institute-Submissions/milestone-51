from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

# Cart contexts: loop through cart items &
# multiply their item quantity by price


def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    cart_plus_ship = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'cart_plus_ship': cart_plus_ship,
    }

    return context
