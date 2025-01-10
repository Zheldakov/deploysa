"""
{% loads %}

"""

from  django import template

register = template.Library() # register


@register.filter()
def user_media(val):
    """Фильтр для замены пути к медиафайлам пользователей на URL адрес из настроек MEDIA_URL."""
    if val:
        return fr"/media/{val}" # Если путь к медиафайлу пользователя не пустой, возвращаем его URL адрес
    return '/static/noavatar.png' # Если путь к медиафайлу пользователя пустой, возвращаем статический дефолтный изображение