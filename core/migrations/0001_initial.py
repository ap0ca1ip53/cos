# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('posicao_operacional', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('equipe', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Executores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('equipe', models.ForeignKey(to='core.Equipe')),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Instalacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=50)),
                ('sigla', models.CharField(max_length=5)),
                ('orgao', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeEquipamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=50)),
                ('nivelTensao', models.CharField(max_length=30)),
                ('imagem', models.ImageField(upload_to=b'upload/equipamentos/')),
            ],
        ),
        migrations.AddField(
            model_name='executores',
            name='funcionario',
            field=models.ForeignKey(to='core.Funcionario'),
        ),
        migrations.AddField(
            model_name='equipamento',
            name='instalacao',
            field=models.ForeignKey(to='core.Instalacao'),
        ),
        migrations.AddField(
            model_name='equipamento',
            name='tipo_de_equipamento',
            field=models.ForeignKey(to='core.TipoDeEquipamento'),
        ),
    ]
