# Generated by Django 3.0.8 on 2020-07-28 00:16

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word_count', '0004_auto_20200724_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_words', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
