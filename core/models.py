from django.db import models
from django.contrib.auth.models import User

STATUS = (
    ('S', 'Solicitada'),
    ('A', 'Em andamento'),
    ('X', 'Cancelada'),
    ('C', 'Concluida'),
)

class Equipe(models.Model):
    equipe = models.CharField(max_length=50)

    def __unicode__(self):
        return self.equipe


class Funcionario(models.Model):
    usuario = models.OneToOneField(User)
    equipe = models.ForeignKey(Equipe)
    nome = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome


class Instalacao(models.Model):
    descricao = models.CharField(max_length=50)
    sigla = models.CharField(max_length=5)
    orgao = models.CharField(max_length=20)
    cidade = models.CharField(max_length=40)

    def __unicode__(self):
        return self.sigla


class TipoDeEquipamento(models.Model):
    descricao = models.CharField(max_length=50)
    nivelTensao = models.CharField(max_length=30)
    imagem = models.ImageField(upload_to='upload/equipamentos/')

    def __unicode__(self):
        return self.descricao

class Equipamento(models.Model):
    instalacao=models.ForeignKey(Instalacao)
    tipo_de_equipamento = models.ForeignKey(TipoDeEquipamento)
    posicao_operacional = models.CharField(max_length=50)

    def __unicode__(self):
        return u"%s de %s" %(self.posicao_operacional, self.instalacao)


class Executores(models.Model):
    funcionario = models.ForeignKey(Funcionario)


class OS(models.Model):
    usuario_criador = models.ForeignKey(User)
    resumo_do_problema = models.CharField(max_length=50)
    descricao_detalhada = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_prevista = models.DateTimeField()
    data_da_execucao = models.DateTimeField(blank=True, null=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS, default='S')
    equipe_destinatario = models.ForeignKey(Equipe)
    equipamento_por_os = models.ManyToManyField(Equipamento)

    def __unicode__(self):
        return self.resumo_do_problema

    def status_verbose(self):
        return dict(STATUS)[self.status]