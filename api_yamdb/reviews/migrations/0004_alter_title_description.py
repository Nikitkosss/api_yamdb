# Generated by Django 3.2 on 2023-05-20 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20230520_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание'),
        ),
    ]
