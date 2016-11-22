from django.db import models


class CastingTime(models.Model):
    text = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['text']


class Duration(models.Model):
    text = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['text']


class SpellRange(models.Model):
    text = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['text']


class School(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(
        max_length=20,
        unique=True,
        help_text='A lable for URL config',)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class CharClass(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(
        max_length=20,
        unique=True,
        help_text='A lable for URL config',)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Level(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(
        max_length=20,
        unique=True,
        help_text='A lable for URL config',)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Source(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(
        max_length=20,
        unique=True,
        help_text='A lable for URL config',)
    link = models.URLField(max_length=255)
    public = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class SpellSource(models.Model):
    source = models.ForeignKey('Source', on_delete=models.CASCADE)
    spell = models.ForeignKey('Spell', on_delete=models.CASCADE)
    page = models.CharField(max_length=20)

    def __str__(self):
        return "{} found in {} on page {}".format(
            self.source, self.spell, self.page)

    class Meta:
        ordering = ['source', 'spell']


class Component(models.Model):
    text = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['text']


class SpellComponent(models.Model):
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    spell = models.ForeignKey('Spell', on_delete=models.CASCADE)
    text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "{} requires {}".format(self.spell, self.text)

    class Meta:
        ordering = ['component']


class Spell(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(
        max_length=100,
        unique=True,
        help_text='A lable for URL config',)
    text = models.TextField()
    ritual = models.BooleanField()
    concentration = models.BooleanField()
    casting_time = models.ForeignKey('CastingTime', on_delete=models.CASCADE)
    duration = models.ForeignKey('Duration', on_delete=models.CASCADE)
    spell_range = models.ForeignKey('SpellRange', on_delete=models.CASCADE)
    school = models.ForeignKey('school', on_delete=models.CASCADE)
    char_class = models.ForeignKey('CharClass', on_delete=models.CASCADE)
    level = models.ForeignKey('Level', on_delete=models.CASCADE)
    source = models.ManyToManyField(
        'Source',
        through='SpellSource',
        related_name='source')
    component = models.ManyToManyField(
        'Component',
        through='SpellComponent',
        related_name='component')
