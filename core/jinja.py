"""
File which stores all variables and functions available in jinja templates.
"""
from django.conf import settings
from django.middleware.csrf import get_token
from django.urls import reverse
from django.utils import translation
from django.utils.timezone import now
from jinja2 import Environment

# from constance import config
#
# from utils.datetime import date
# from utils.rst import rst
from utils.static import static
# from utils.images import ImageProcessor, Resize


context = {
    'globals': {
        'DEBUG': settings.DEBUG,
        'LANG': settings.LANGUAGE_CODE,

        'static': static,
        # 'media': lambda file: settings.MEDIA_URL + file,
        'csrf_token': get_token,
        'url': reverse,
        # 'now': now,
        # 'constance': config,
    },
    'filters': {
        # 'rst': rst,
        # 'date': date,
        # 'thumb': lambda img, w, h: ImageProcessor(operations=[Resize(size=(w, h))])(img),
    },
}


def environment(**options):
    env = Environment(**options, extensions=['jinja2.ext.i18n'])
    env.autoescape = True
    env.install_gettext_translations(translation, newstyle=True)

    env.globals.update(context['globals'])
    env.filters.update(context['filters'])

    return env
