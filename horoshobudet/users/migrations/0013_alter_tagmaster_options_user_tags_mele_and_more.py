# Generated by Django 5.0.6 on 2024-07-01 14:55

import taggit.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        ('users', '0012_alter_tagmaster_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tagmaster',
            options={'ordering': ['tag'], 'verbose_name': 'Тэг', 'verbose_name_plural': 'Навыки (тэги)'},
        ),
        migrations.AddField(
            model_name='user',
            name='tags_mele',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='tagmaster',
            name='tag',
            field=models.CharField(db_index=True, max_length=100, verbose_name='навык'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='users.tagmaster', verbose_name='Навыки'),
        ),
    ]
