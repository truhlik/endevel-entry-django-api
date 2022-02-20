from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.template.defaultfilters import truncatechars  # or truncatewords


# Create your models here.


class Tag(models.Model):
    name = models.CharField(_("Name"), max_length=100,
                            null=True, blank=True, default=None)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Article(models.Model):
    title_en = models.CharField(_("Title EN"), max_length=100,
                                null=True, blank=True, default=None)
    title_cz = models.CharField(_("Title CZ"), max_length=100,
                                null=True, blank=True, default=None)
    content_en = models.TextField(
        _("Content EN"), null=True, blank=True, default=None)
    content_cz = models.TextField(
        _("Content CZ"), null=True, blank=True, default=None)
    header_image = models.ImageField(
        _("Header Image"), upload_to='uploads/', blank=True, null=True, default=None)
    header_thumb = models.CharField(_("Header Thumbnail"), max_length=100,
                                    null=True, blank=True, default=None)
    tags = models.ManyToManyField(Tag)

    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title_en
    @property
    def short_content_en(self):
        return truncatechars(self.content_en, 30)

    @property
    def short_content_cz(self):
        return truncatechars(self.content_cz, 30)
