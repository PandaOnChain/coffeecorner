from django import template

register = template.Library()


@register.filter
def range_filter(value):
    return range(int(value)-1)




@register.filter
def empty_stars(value):
    return int(value)-5

@register.filter
def remain_stars(value):
    return range(5 - int(value))