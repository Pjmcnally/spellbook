from django.shortcuts import render

from .models import Spell, SpellSource


# Create your views here.
def display_spell(request, spell):
    spell = Spell.objects.get(slug=spell)
    context = {'spell': spell}
    return render(request, 'spellbook_app/spell.html', context)
