# Generated by Django 5.0.6 on 2024-06-06 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0002_uploadfiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото работ'),
        ),
    ]
