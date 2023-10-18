# Third Party Library
from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    """Добавляет класс полю."""
    return field.as_widget(attrs={"class": css})


@register.filter()
def to_int(value):
    """Конвертирует полученное значение в целое число."""
    try:
        value = int(value)
    except ValueError:
        pass
    except TypeError:
        pass
    return value


@register.filter()
def convert_to_point(value):
    """Заменяет запятую в числе на точку."""
    return value.replace(",", ".")


@register.filter()
def multiply(a, b):
    """Умножает два числа."""
    if a == "" or a is None:
        a = 0
    if b == "" or b is None:
        b = 0
    return float(a) * float(b)
