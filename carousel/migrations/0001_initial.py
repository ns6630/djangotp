# Generated by Django 3.1.2 on 2020-10-11 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselSlide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carousel', verbose_name='Изображение')),
                ('is_active', models.BooleanField(default=True, verbose_name='Является ли активным')),
                ('order', models.IntegerField(verbose_name='Номер слайда в карусели')),
            ],
            options={
                'verbose_name': 'Слайд карусели',
                'verbose_name_plural': 'Слайды карусели',
            },
        ),
    ]
