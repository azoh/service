# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('failure', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='awaria',
            name='update_date',
        ),
        migrations.AddField(
            model_name='awaria',
            name='remove_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data zakończenia naprawy'),
        ),
        migrations.AddField(
            model_name='awaria',
            name='repair_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data rozpoczęcia naprawy'),
        ),
        migrations.AlterField(
            model_name='awaria',
            name='status',
            field=models.ForeignKey(to='failure.Status', default=1, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='awaria',
            name='sur',
            field=models.CharField(blank=True, null=True, verbose_name='Przyjęte przez', max_length=50),
        ),
        migrations.AlterField(
            model_name='awaria',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Zgłaszający'),
        ),
    ]
