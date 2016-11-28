from django.conf.urls import url

from .views import display_spell

urlpatterns = [
    url(r'spell/(?P<spell>[\w-]+)', display_spell, name='display_spell'),
]
