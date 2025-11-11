from django import template
from ..models import Order

register = template.Library()

@register.simple_tag(name="net_price")
def net_price(orders):
    net_amount = 0
    for order in orders:
        if order.product and order.product.new_price:
            net_amount += order.quantity * order.product.new_price
    return net_amount

@register.simple_tag(name="discount_price")
def discount_price(orders):
    total_discount = 0
    for order in orders:
        if order.product and order.product.offer:
            total_discount += order.quantity * order.product.offer
    return total_discount

@register.simple_tag(name="total_price")
def total_price(orders):
    net_amount = net_price(orders)
    total_discount = discount_price(orders)
    total_amount = net_amount - total_discount
    return total_amount
