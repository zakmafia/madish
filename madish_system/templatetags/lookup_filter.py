from django import template

register = template.Library()

@register.filter()
def lookup(d, key):
    return d[key]

@register.filter(name='times')
def times(number):
    return range(number)
