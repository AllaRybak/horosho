# Generated by Django 5.0.6 on 2024-06-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0008_photos_text_alter_photos_contract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='cat',
            field=models.ManyToManyField(blank=True, to='masters.category', verbose_name='Навык'),
        ),
    ]
