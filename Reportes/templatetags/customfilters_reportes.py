from django import template
from django.contrib.auth.models import *


register = template.Library()

@register.filter(name='getfullname')
def getfullname(data):

    name = data.get_full_name()
    return name
    
    
@register.filter(name='getname')   
def getname(pk):
    name=""
    if pk:
        try:
            u = User.objects.get(id=pk)
            name = u.get_full_name()
        except: pass
    else: name=""
    return name