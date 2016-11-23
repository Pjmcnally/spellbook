from django.db import models


class CastingTime(models.Model):
    text = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(
        max_length=100,
        unique=True,
        help_text='A label for URL config')

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['text']


class Class(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(
        max_length=20,
        unique=True,
        help_text='A lable for URL config',)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Component(models.Model):
    full_name = models.CharField(max_length=20, unique=True)
    short_name = models.CharField(max_length=1, unique=True)
    slug = models.SlugField(
        max_length=20,
        unique=True,
        help_text='A lable for URL config',)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['full_name']


class Domain(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(
        max_length=20,
        unique=True,
        help_text='A lable for URL config',)
    _class = models.ForeignKey('Class', on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self._class, self.name)

    class Meta:
        ordering = ['_class', 'name']


class Duration(models.Model):
    text = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(
        max_length=100,
        unique=True,
        help_text='A label for URL config')

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['text']


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


class Range(models.Model):
    text = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(
        max_length=100,
        unique=True,
        help_text='A label for URL config')

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


class Source(models.Model):
    full_name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(
        max_length=20,
        unique=True,
        help_text='A lable for URL config',)
    link = models.URLField(max_length=255)
    public = models.BooleanField()

    def __str__(self):
        return self.short_name

    class Meta:
        ordering = ['short_name']


class SpellSource(models.Model):
    source = models.ForeignKey('Source', on_delete=models.CASCADE)
    spell = models.ForeignKey('Spell', on_delete=models.CASCADE)
    page = models.CharField(max_length=20)

    def __str__(self):
        return "{} found in {} on page {}".format(
            self.source, self.spell, self.page)

    class Meta:
        ordering = ['source', 'spell']


class Spell(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(
        max_length=100,
        unique=True,
        help_text='A lable for URL config',)
    text = models.TextField()
    concentration = models.BooleanField()
    ritual = models.BooleanField()

    cast_time_misc = models.CharField(max_length=100)
    component_misc = models.CharField(max_length=100)
    range_misc = models.CharField(max_length=100)

    casting_time = models.ForeignKey('CastingTime', on_delete=models.CASCADE)
    duration = models.ForeignKey('Duration', on_delete=models.CASCADE)
    level = models.ForeignKey('Level', on_delete=models.CASCADE)
    _range = models.ForeignKey('Range', on_delete=models.CASCADE)
    school = models.ForeignKey('school', on_delete=models.CASCADE)

    _class = models.ManyToManyField(
        'Class',
        related_name="_class")
    component = models.ManyToManyField(
        'Component',
        related_name='component')
    domain = models.ManyToManyField(
        'Domain',
        related_name='domain',
        blank=True)
    source = models.ManyToManyField(
        'Source',
        through='SpellSource',
        related_name='source')

    def __str__(self):
        return self.name

    def output_json(self):
        # check out https://docs.djangoproject.com/en/1.10/topics/files/
        pass
