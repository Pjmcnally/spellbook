from django.shortcuts import render

from .models import Clss, Spell


def spell_list(request, slug=None):
    classes = Clss.objects.all()  # get all classes for navbar
    if slug:
        class_obj = Clss.objects.get(slug__iexact=slug)
        spells = class_obj.spells.filter(source__public=True)
    else:
        spells = Spell.objects.filter(source__public=True)

    # For my data at the moment the method of using a dict to sort
    # as opposed to .filter for each level seems faster so I am using it
    spell_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [],
                  8: [], 9: []}

    for spell in spells:
        spell_dict[spell.level.num].append(spell)

    context = {
        'classes': classes,
        'spells': spell_dict}

    return render(request, 'spellbook/spell_list.html', context)


def spell_detail(request, slug):
    classes = Clss.objects.all()  # get all classes for navbar
    spell = Spell.objects.get(slug=slug)
    context = {'classes': classes, 'spell': spell}
    return render(request, 'spellbook/spell_detail.html', context)
