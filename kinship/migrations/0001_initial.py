# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kinship',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('kinship_type', models.CharField(max_length=32)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.DateTimeField(null=True)),
                ('birth_location', models.CharField(max_length=50, blank=True)),
                ('affiliation', models.CharField(max_length=32, blank=True)),
                ('biography_link', models.URLField(blank=True)),
                ('is_public', models.BooleanField(default=True)),
                ('affiliation_update', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ego_position', models.CharField(max_length=50)),
                ('action_type', models.CharField(max_length=20)),
                ('appointee_position', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('start_exercise', models.DateTimeField(null=True)),
                ('end_exercise', models.DateTimeField(null=True)),
                ('appointee', models.ForeignKey(to='kinship.Person', related_name='appointee')),
                ('ego', models.ForeignKey(to='kinship.Person', related_name='ego_')),
            ],
        ),
        migrations.AddField(
            model_name='kinship',
            name='ego',
            field=models.ForeignKey(to='kinship.Person', related_name='ego'),
        ),
        migrations.AddField(
            model_name='kinship',
            name='godfather',
            field=models.ForeignKey(to='kinship.Person', related_name='godfather'),
        ),
        migrations.AddField(
            model_name='kinship',
            name='godmother',
            field=models.ForeignKey(to='kinship.Person', related_name='godmother'),
        ),
    ]
