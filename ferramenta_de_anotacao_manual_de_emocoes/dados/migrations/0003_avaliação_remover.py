# Generated by Django 4.2.11 on 2024-05-05 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0002_remove_text_admiração_remove_text_alegria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliação',
            name='Remover',
            field=models.BooleanField(default=False, verbose_name='Remover'),
        ),
    ]
