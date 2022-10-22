from django import template
register = template.Library()

@register.filter
def upper(dicts,key):
    
  return len(dicts[f"{key}"])