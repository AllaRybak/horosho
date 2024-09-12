# Generated by Django 5.0.6 on 2024-07-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_alter_comment_options_alter_contactus_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(max_length=100, verbose_name='Тема обращения'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='text_mes',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]
