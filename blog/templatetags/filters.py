from django import template

register = template.Library()


@register.filter("times")
def times(value):
    for _ in range(value):
        yield _


@register.filter("filter_range")
def filter_range(start, end):
    for _ in range(start, end):
        yield _
