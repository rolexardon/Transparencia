from django import template

register = template.Library()

@register.filter(name='getfullname')
def getfullname(data):

    name = data.get_full_name()
    return name