from django import template

register = template.Library()

def split(value):
    """Removes all values of arg from the given string"""
    return value.split(",")

register.filter("split", split)