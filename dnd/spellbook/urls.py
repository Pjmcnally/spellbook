from django.conf.urls import url

from .views import spell_detail, spell_list, spell_content

urlpatterns = [
    url(r'^$', spell_list, name='spell_list'),
    url(r'^spell_content$', spell_content, name='spell_content'),
    url(r'^spell/(?P<slug>[\w-]+)/$', spell_detail, name='spell_detail'),
]
