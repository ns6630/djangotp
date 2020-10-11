from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from PIL import Image
import os


class CarouselSlide(models.Model):
    image = models.ImageField(verbose_name='Изображение', upload_to='carousel')
    is_active = models.BooleanField(verbose_name='Является ли активным', default=True)
    order = models.IntegerField(verbose_name='Номер слайда в карусели')

    def save(self):        
        super(CarouselSlide, self).save()

        max_image_size = 640, 480
        with Image.open(self.image) as img:
            img.thumbnail(max_image_size)
            img.save(self.image.path)

    class Meta:
        verbose_name = 'Слайд карусели'
        verbose_name_plural = 'Слайды карусели'

    def __str__(self):
        return f'Сладер с номером {self.order}. Активность: {self.is_active}.'


@receiver(post_delete, sender=CarouselSlide)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
