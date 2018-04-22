from django import template

register = template.Library()

@register.filter(name = 'xxx')
def cut(value , arg):
    '''
    this cut the value from arg
    '''
    return value.replace(arg,'')
