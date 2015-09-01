# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150825_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='os',
            name='data_da_execucao',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
