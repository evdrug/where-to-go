# Generated by Django 3.1 on 2020-09-28 15:48

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.CharField(blank=True, max_length=300, verbose_name='Краткое описание'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('position', models.IntegerField(verbose_name='Позиция')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='Место')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]