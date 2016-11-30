from django.shortcuts import render

from .models import Class, Spell


def spell_list(request):
    classes = Class.objects.all()
    context = {'classes': classes}
    return render(request, 'spellbook_app/spell_list.html', context)


# Create your views here.
def spell_detail(request, spell):
    spell = Spell.objects.get(slug=spell)
    context = {'spell': spell}
    return render(request, 'spellbook_app/spell_detail.html', context)
