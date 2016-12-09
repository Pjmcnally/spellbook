from django.shortcuts import render

from .models import Clss, Spell


def spell_list(request, slug=None):
    """ function to render spell list page """
    classes = Clss.objects.all()  # get all classes for navbar
    if slug:
        class_obj = Clss.objects.get(slug__iexact=slug)
        spells = class_obj.spells.filter(source__public=True)
    else:
        spells = Spell.objects.filter(source__public=True)

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

    spell_dict = {
        0: cantrips,
        1: spells_1,
        2: spells_2,
        3: spells_3,
        4: spells_4,
        5: spells_5,
        6: spells_6,
        7: spells_7,
        8: spells_8,
        9: spells_9,
    }

    context = {
        'classes': classes,
        'spells': spell_dict}

    return render(request, 'spellbook/spell_list.html', context)


def spell_detail(request, slug):
    classes = Clss.objects.all()  # get all classes for navbar
    spell = Spell.objects.get(slug=slug)
    context = {'classes': classes, 'spell': spell}
    return render(request, 'spellbook/spell_detail.html', context)
