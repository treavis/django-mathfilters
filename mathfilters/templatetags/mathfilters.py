from __future__ import print_function, division, absolute_import, unicode_literals
from django.template import Library
from decimal import Decimal

register = Library()


def valid_numeric(arg):
    if isinstance(arg, (int, float, Decimal)):
        return arg
    try:
        return int(arg)
    except ValueError:
        return float(arg)


@register.filter
def sub(value, arg):
    """Subtract the arg from the value."""
    try:
        return valid_numeric(value) - valid_numeric(arg)
    except (ValueError, TypeError):
        try:
            return value - arg
        except Exception:
            return ''
sub.is_safe = False


@register.filter
def mul(value, arg):
    """Multiply the arg with the value."""
    try:
        return valid_numeric(value) * valid_numeric(arg)
    except (ValueError, TypeError):
        try:
            return value * arg
        except Exception:
            return ''
mul.is_safe = False


@register.filter()
def div(value, arg):
    """Divide the arg by the value."""
    try:
        return valid_numeric(value) / valid_numeric(arg)
    except (ValueError, TypeError):
        try:
            return value / arg
        except Exception:
            return ''
div.is_safe = False


@register.filter(name='abs')
def absolute(value):
    """Return the absolute value."""
    try:
        return abs(valid_numeric(value))
    except (ValueError, TypeError):
        try:
            return abs(value)
        except Exception:
            return ''
absolute.is_safe = False


@register.filter()
def mod(value, arg):
    """Return the modulo value."""
    try:
        return valid_numeric(value) % valid_numeric(arg)
    except (ValueError, TypeError):
        try:
            return value % arg
        except Exception:
            return ''
mod.is_safe = False
