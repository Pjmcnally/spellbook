from django.db import models
from django.core.urlresolvers import reverse


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
        return self.name.title()

    def get_absolute_url(self):
        return reverse('class_spell_list', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class Component(models.Model):
    full_name = models.CharField(max_length=20, unique=True)
    short_name = models.CharField(max_length=1, unique=True)
    count = models.SmallIntegerField(unique=True)  # A field to aid in arbitrary sorting
    slug = models.SlugField(
        max_length=1,
        unique=True,
        help_text='A lable for URL config',)

    def __str__(self):
        return self.short_name

    class Meta:
        ordering = ['count']


class Domain(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(
        max_length=20,
        unique=True,
        help_text='A lable for URL config',)

    def __str__(self):
        return self.name.title()

    class Meta:
        ordering = ['name']


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
    text = models.CharField(max_length=20, unique=True)
    ord_text = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(
        max_length=20,
        unique=True,
        help_text='A lable for URL config',)
    num = models.SmallIntegerField()

    def __str__(self):
        return self.ord_text

    class Meta:
        ordering = ['num']


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
        return self.name.title()

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

    spells = models.ManyToManyField(
        'spell', through='SpellSource')

    def __str__(self):
        return self.short_name

    class Meta:
        ordering = ['short_name']


class SpellSource(models.Model):
    spell = models.ForeignKey('Spell', on_delete=models.CASCADE)
    source = models.ForeignKey('Source', on_delete=models.CASCADE)
    page = models.CharField(max_length=20)

    class Meta:
        ordering = ['source', 'spell']


class SubDomain(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(
        max_length=20,
        help_text='A lable for URL config',)
    domain = models.ForeignKey('Domain', on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.domain, self.name.title())

    class Meta:
        unique_together = (('slug', 'domain'), ('name', 'domain'))
        ordering = ['domain', 'name']


class Spell(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(
        max_length=100,
        unique=True,
        help_text='A lable for URL config',)
    text = models.TextField()
    concentration = models.BooleanField()
    ritual = models.BooleanField()

    cast_time_text = models.CharField(max_length=100, null=True)
    component_text = models.CharField(max_length=100, null=True)
    range_text = models.CharField(max_length=100, null=True)

    casting_time = models.ForeignKey('CastingTime', on_delete=models.CASCADE)
    duration = models.ForeignKey('Duration', on_delete=models.CASCADE)
    level = models.ForeignKey('Level', on_delete=models.CASCADE)
    rng = models.ForeignKey('Range', on_delete=models.CASCADE)
    school = models.ForeignKey('School', on_delete=models.CASCADE)

    clss = models.ManyToManyField(
        'Class',
        related_name="_class")
    component = models.ManyToManyField(
        'Component',
        related_name='component')
    sub_domain = models.ManyToManyField(
        'SubDomain',
        related_name='sub_domain',
        blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['level', 'name']

    def output_json(self):
        # check out https://docs.djangoproject.com/en/1.10/topics/files/
        pass

    def get_absolute_url(self):
        return reverse('spell_detail', kwargs={'slug': self.slug})
