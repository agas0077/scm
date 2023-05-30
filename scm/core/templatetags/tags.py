from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})

@register.filter
def concat(arg1, arg2):
    return str(arg1) + str(arg2)