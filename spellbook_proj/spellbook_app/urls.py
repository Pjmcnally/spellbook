from django.conf.urls import url

from .views import spell_detail, spell_list

urlpatterns = [
    url(r'^$', spell_list, name='spell_list'),
    url(r'spell/(?P<spell>[\w-]+)/$', spell_detail, name='spell_detail'),
]
