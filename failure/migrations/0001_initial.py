# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Awaria',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='Opis awarii')),
                ('add_date', models.DateTimeField(verbose_name='Data zgłoszenia', auto_now_add=True)),
                ('sur', models.TextField(blank=True, verbose_name='Przyjęte przez', null=True)),
                ('update_date', models.DateTimeField(verbose_name='Data ostaniej modyfikacji', auto_now=True)),
            ],
            options={
                'verbose_name': 'Awaria',
                'verbose_name_plural': 'Awarie',
            },
        ),
        migrations.CreateModel(
            name='Hala',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('symbol', models.CharField(verbose_name='Symbol hali', max_length=10)),
                ('user', models.ForeignKey(verbose_name='Opiekun', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Hala',
                'verbose_name_plural': 'Hale',
            },
        ),
        migrations.CreateModel(
            name='Maszyna',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nazwa', models.CharField(verbose_name='Nazwa', max_length=50)),
                ('hala', models.ForeignKey(verbose_name='Hala', to='failure.Hala')),
                ('opiekun', models.ForeignKey(default=1, verbose_name='Opiekun', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Maszyna',
                'verbose_name_plural': 'Maszyny',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nazwa', models.CharField(verbose_name='Nazwa', max_length=50)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Statusy',
            },
        ),
        migrations.CreateModel(
            name='Wydzial',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nazwa', models.CharField(verbose_name='Nazwa wydziału', max_length=50)),
                ('user', models.ForeignKey(verbose_name='Mistrz', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Wydział',
                'verbose_name_plural': 'Wydziały',
            },
        ),
        migrations.AddField(
            model_name='maszyna',
            name='wydzial',
            field=models.ForeignKey(verbose_name='Wydział', to='failure.Wydzial'),
        ),
        migrations.AddField(
            model_name='awaria',
            name='maszyna',
            field=models.ForeignKey(to='failure.Maszyna', verbose_name='Maszyna', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='awaria',
            name='status',
            field=models.ForeignKey(default=4, verbose_name='Status', to='failure.Status'),
        ),
        migrations.AddField(
            model_name='awaria',
            name='user',
            field=models.ForeignKey(verbose_name='Użytkownik', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='awaria',
            name='wydzial',
            field=models.ForeignKey(verbose_name='Wydział', to='failure.Wydzial'),
        ),
    ]
