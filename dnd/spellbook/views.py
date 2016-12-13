from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Clss, Spell


@ensure_csrf_cookie
def spell_list(request, slug=None):
    """ function to render spell list page """
    class_obj = None
    classes = Clss.objects.all()  # get all classes for navbar

    context = {
        'class': class_obj,
        'classes': classes}

    return render(request, 'spellbook/spell_list.html', context)


def spell_detail(request, slug):
    classes = Clss.objects.all()  # get all classes for navbar
    spell = Spell.objects.get(slug=slug)
    context = {'classes': classes, 'spell': spell}
    return render(request, 'spellbook/spell_detail.html', context)


def spell_content(request):
    if request.method == 'POST':

        clss = request.POST.get("class", None)
        if clss:
            class_obj = Clss.objects.get(slug__iexact=clss)
            spells = class_obj.spells.filter(source__public=True)
        else:
            spells = Spell.objects.filter(source__public=True)

        search = request.POST.get("search", None)
        if search:
            spells = spells.filter(name__icontains=search)

        spell_dict = {
            0: spells.filter(level__num=0),
            1: spells.filter(level__num=1),
            2: spells.filter(level__num=2),
            3: spells.filter(level__num=3),
            4: spells.filter(level__num=4),
            5: spells.filter(level__num=5),
            6: spells.filter(level__num=6),
            7: spells.filter(level__num=7),
            8: spells.filter(level__num=8),
            9: spells.filter(level__num=9),
        }

        context = {
            'spells': spell_dict}
    else:
        return HttpResponse("")

    return render(request, 'spellbook/spell_content.html', context)
