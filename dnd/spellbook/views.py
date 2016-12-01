from django.shortcuts import render

from .models import Class, Spell


def spell_list(request, slug=None):
    classes = Class.objects.all()  # get all classes for navbar
    if slug:
        title_text = Class.objects.get(slug__iexact=slug).name.title()
        spells = Spell.objects.filter(_class__slug=slug) \
                              .filter(source__public=True)
    else:
        title_text = "All"
        spells = Spell.objects.all().filter(source__public=True)

    context = {'classes': classes, 'spells': spells, "title_text": title_text}
    return render(request, 'spellbook/spell_list.html', context)


def spell_detail(request, slug):
    classes = Class.objects.all()  # get all classes for navbar
    spell = Spell.objects.get(slug=slug)
    context = {'classes': classes, 'spell': spell}
    return render(request, 'spellbook/spell_detail.html', context)