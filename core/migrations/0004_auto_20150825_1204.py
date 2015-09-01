# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_os'),
    ]

    operations = [
        migrations.AlterField(
            model_name='os',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='os',
            name='data_ultima_atualizacao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='os',
            name='usuario_criador',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
