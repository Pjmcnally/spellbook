from django.shortcuts import render

from .models import Class, Spell


def spell_list(request, slug=None):
    classes = Class.objects.all()  # get all classes for navbar
    if slug:
        title_text = Class.objects.get(slug__iexact=slug).name.title()
        spells = Spell.objects.filter(_class__slug=slug)  # \
                              # .filter(source__public=True)
    else:
        title_text = "All"
        spells = Spell.objects.all()  # .filter(source__public=True)

    cantrips = spells.filter(level__num=0)
    spells_1 = spells.filter(level__num=1)
    spells_2 = spells.filter(level__num=2)
    spells_3 = spells.filter(level__num=3)
    spells_4 = spells.filter(level__num=4)
    spells_5 = spells.filter(level__num=5)
    spells_6 = spells.filter(level__num=6)
    spells_7 = spells.filter(level__num=7)
    spells_8 = spells.filter(level__num=8)
    spells_9 = spells.filter(level__num=9)

    context = {
        'classes': classes,
        'title_text': title_text,
        'cantrips': cantrips,
        'spells_1': spells_1,
        'spells_2': spells_2,
        'spells_3': spells_3,
        'spells_4': spells_4,
        'spells_5': spells_5,
        'spells_6': spells_6,
        'spells_7': spells_7,
        'spells_8': spells_8,
        'spells_9': spells_9,}
    return render(request, 'spellbook/spell_list.html', context)


def spell_detail(request, slug):
    classes = Class.objects.all()  # get all classes for navbar
    spell = Spell.objects.get(slug=slug)
    context = {'classes': classes, 'spell': spell}
    return render(request, 'spellbook/spell_detail.html', context)
