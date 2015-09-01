# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_funcionario_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resumo_do_problema', models.CharField(max_length=50)),
                ('descricao_detalhada', models.TextField()),
                ('data_criacao', models.DateTimeField()),
                ('data_prevista', models.DateTimeField()),
                ('data_da_execucao', models.DateTimeField()),
                ('data_ultima_atualizacao', models.DateTimeField()),
                ('status', models.CharField(default=b'S', max_length=1, choices=[(b'S', b'Solicitada'), (b'A', b'Em andamento'), (b'X', b'Cancelada'), (b'C', b'Concluida')])),
                ('equipamento_por_os', models.ManyToManyField(to='core.Equipamento')),
                ('equipe_destinatario', models.ForeignKey(to='core.Equipe')),
                ('usuario_criador', models.ForeignKey(to='core.Funcionario')),
            ],
        ),
    ]
