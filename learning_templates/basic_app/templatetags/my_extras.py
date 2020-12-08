from django import template

register = template.Library()
#2. Registering the filter using Decorators
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all the values of "arg" from the string!
    """
    return value.replace(arg,"")
#1. Normal way of registering the filter below
# register.filter('cut',cut)
