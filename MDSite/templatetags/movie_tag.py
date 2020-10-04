from django import template
from MDSite.models import alle


register = template.Library()


@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return alle.objects.all()


@register.inclusion_tag('MDSite/index.html')
def get_last_movies(count=5):
    MDSite = alle.objects.order_by("id")[:count]
    return {"last_movies": movies}
