# coding: utf-8

from views import *
from django.conf.urls import include, url

urlpatterns = [
        url(r'^$', HomeView.as_view(), name='home'),

        # Instalações
        url(r'^instalacoes/$', InstalacaoList.as_view(), name='instalacao_list'),
        url(r'^instalacoes/add/$', InstalacaoCreate.as_view(), name='instalacao_add'),
        url(r'^instalacoes/(?P<pk>\d+)/$', InstalacaoDetail.as_view(), name='instalacao_detail'),
        url(r'^instalacoes/edit/(?P<pk>\d+)/$', InstalacaoUpdate.as_view(), name='instalacao_update'),
        url(r'^instalacoes/delete/(?P<pk>\d+)/$', InstalacaoDelete.as_view(), name='instalacao_del'),

        url(r'^equipes/$', EquipeList.as_view(), name='equipe_list'),
        url(r'^equipes/add/$', EquipeCreate.as_view(), name='equipe_add'),
        url(r'^equipes/edit/(?P<pk>\d+)/$', EquipeUpdate.as_view(), name='equipe_update'),
        url(r'^equipes/delete/(?P<pk>\d+)/$', EquipeDelete.as_view(), name='equipe_del'),

        url(r'^tipodeequipamento/$', TipoDeEquipamentoList.as_view(), name='tipodeequipamento_list'),
        url(r'^tipodeequipamento/add/$', TipoDeEquipamentoCreate.as_view(), name='tipodeequipamento_add'),
        url(r'^tipodeequipamento/(?P<pk>\d+)/$', TipoDeEquipamentoDetail.as_view(), name='tipodeequipamento_detail'),
        url(r'^tipodeequipamento/edit/(?P<pk>\d+)/$', TipoDeEquipamentoUpdate.as_view(), name='tipodeequipamento_update'),
        url(r'^tipodeequipamento/delete/(?P<pk>\d+)/$', TipoDeEquipamentoDelete.as_view(), name='tipodeequipamento_del'),

        url(r'^equipamento/$', EquipamentoList.as_view(), name='equipamento_list'),
        url(r'^equipamento/add/$', EquipamentoCreate.as_view(), name='equipamento_add'),
        url(r'^equipamento/edit/(?P<pk>\d+)/$', EquipamentoUpdate.as_view(), name='equipamento_update'),
        url(r'^equipamento/delete/(?P<pk>\d+)/$', EquipamentoDelete.as_view(), name='equipamento_del'),

        url(r'^funcionario/$', FuncionarioList.as_view(), name='funcionario_list'),
        url(r'^funcionario/add/$', FuncionarioCreate.as_view(), name='funcionario_add'),
        url(r'^funcionario/edit/(?P<pk>\d+)/$', FuncionarioUpdate.as_view(), name='funcionario_update'),
        url(r'^funcionario/delete/(?P<pk>\d+)/$', FuncionarioDelete.as_view(), name='funcionario_del'),

        url(r'^os/$', OSList.as_view(), name='os_list'),
        url(r'^os/add/$', OSCreate.as_view(), name='os_add'),
        url(r'^os/cancel/(?P<pk>\d+)/$', OSCancelar.as_view(), name='os_cancelar'),
        
]