# ~*~ coding: utf-8 ~*~
from django.db import models


class Image(models.Model):
    title = models.CharField('Название', max_length=256)
    dsc = models.CharField('Описание', max_length=250, blank=True)
    image = models.ImageField(upload_to='gallery', null=False, blank=False)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.image.url

    def save(self, force_insert=False, force_update=False, using=None):
        try:
            obj = Image.objects.get(id=self.id)
            if obj.image.path != self.image.path:
                obj.image.delete()
        except:
            pass
        super(Image, self).save()

    def delete(self, using=None):
        try:
            obj = Image.objects.get(id=self.id)
            obj.image.delete()
        except (Image.DoesNotExist, ValueError):
            pass
        super(Image, self).delete()

    def preview_image_url(self):
        if self.image:
            return u'<img src="%s" width="100"/>' % self.image.url
        else:
            return '(none)'
    preview_image_url.short_description = 'Thumbnail'
    preview_image_url.allow_tags = True
