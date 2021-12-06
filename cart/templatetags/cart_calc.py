from django import template


register = template.Library()

""" 
calculating subtotal when quantity is > 1 in cart of same item 
"""
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity