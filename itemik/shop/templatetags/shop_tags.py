from django import template
import shop.views as views


register = template.Library()


@register.simple_tag()
def navigation_menu():
    return views.navigation_menu
