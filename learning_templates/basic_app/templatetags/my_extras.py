from django import template

# cara pertama untuk "register"
register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    this cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('cut', cut) #ini cara kedua kalau tidak memakai @register
#@register harus ditulis sblm "def cut(value, arg)"
