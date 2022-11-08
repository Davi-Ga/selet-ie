from django import template 

register = template.Library()

@register.filter(name='is_par')
def is_par(value):
    return value % 2 == 0