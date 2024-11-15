import decimal
from django import template
register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    if isinstance(quantity, (int, float, decimal.Decimal)):
        return price * quantity
    else:
        return 0
