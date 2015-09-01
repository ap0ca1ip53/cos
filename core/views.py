from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from models import Instalacao, Equipe, TipoDeEquipamento, Equipamento, Funcionario, OS
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class LoginMixin(object):

    @classmethod
    def as_view(cls, **kwargs):
        view=super(LoginMixin, cls).as_view(**kwargs)
        return login_required(view)


class HomeView(LoginMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context=super(HomeView, self).get_context_data(**kwargs)
        context['OS']=5
        return context


class InstalacaoCreate(LoginMixin, CreateView, SuccessMessageMixin):
    model = Instalacao
    success_url = '/instalacoes/'
    fields = ['sigla', 'descricao', 'orgao', 'cidade']


class InstalacaoList(LoginMixin, ListView):
    model = Instalacao

    
    def get(self, request, *args, **kwargs):
        if Instalacao.objects.count() > 0:
            return super(InstalacaoList, self).get(request, *args, **kwargs)
        else:
            return redirect(reverse('core:instalacao_add'))


class InstalacaoDetail(LoginMixin, DetailView):
    model = Instalacao

    
    def get(self, request, *args, **kwargs):
        if Instalacao.objects.count() > 0:
            return super(InstalacaoDetail, self).get(request, *args, **kwargs)
        else:
            return redirect(reverse('core:instalacao_add'))


class InstalacaoUpdate(LoginMixin, UpdateView, SuccessMessageMixin):
    model = Instalacao
    success_url = '/instalacoes/'
    fields = ['sigla', 'descricao', 'orgao', 'cidade']

    def dispatch(self, *args, **kwargs):
        return super(InstalacaoUpdate, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if Instalacao.objects.count() > 0:
            return super(InstalacaoUpdate, self).get(request, *args, **kwargs)
        else:
            return redirect(reverse('core:instalacao_add'))


class InstalacaoDelete(DeleteView):
    model = Instalacao
    success_url = '/instalacoes/'


class EquipeList(LoginMixin, ListView):
    model = Equipe

    def get(self, request, *args, **kwargs):
        if Equipe.objects.count() > 0:
            return super(EquipeList, self).get(request, *args, **kwargs)
        else:
            return redirect(reverse('core:equipe_add'))


class EquipeCreate(LoginMixin, CreateView):
    model = Equipe
    success_url = '/equipes/'
    fields = ['equipe']

    def dispatch(self, *args, **kwargs):
        return super(EquipeCreate, self).dispatch(*args, **kwargs)


class EquipeUpdate(LoginMixin, UpdateView):
    model = Equipe
    success_url = '/equipes/'
    fields = ['equipe']

    def get(self, request, *args, **kwargs):
        if Equipe.objects.count() > 0:
            return super(EquipeUpdate, self).get(request, *args, **kwargs)
        else:
            return redirect(reverse('core:equipe_add'))


class EquipeDelete(DeleteView):
    model = Equipe
    success_url = '/equipes/'


class TipoDeEquipamentoList(ListView):
    model = TipoDeEquipamento

    def get(self, request, *args, **kwargs):
        if TipoDeEquipamento.objects.count() > 0:
            return super(TipoDeEquipamentoList, self).get(request, *args, **kwargs)
        else:
            return redirect(reverse('core:tipodeequipamento_add'))

    def dispatch(self, *args, **kwargs):
        return super(TipoDeEquipamentoList, self).dispatch(*args, **kwargs)


class TipoDeEquipamentoCreate(LoginMixin, CreateView):
    model = TipoDeEquipamento
    success_url = '/tipodeequipamento/'
    fields = ['descricao', 'nivelTensao', 'imagem']

    def dispatch(self, *args, **kwargs):
        return super(TipoDeEquipamentoCreate, self).dispatch(*args, **kwargs)


class TipoDeEquipamentoUpdate(LoginMixin, UpdateView):
    model = TipoDeEquipamento
    success_url = '/tipodeequipamento/'
    fields = ['descricao', 'nivelTensao', 'imagem']

    def dispatch(self, *args, **kwargs):
        return super(TipoDeEquipamentoUpdate, self).dispatch(*args, **kwargs)


class TipoDeEquipamentoDelete(LoginMixin, DeleteView):
    model = TipoDeEquipamento
    success_url = '/tipodeequipamento/'


class TipoDeEquipamentoDetail(LoginMixin, DetailView):
    model = TipoDeEquipamento

    def dispatch(self, *args, **kwargs):
        return super(TipoDeEquipamentoDetail, self).dispatch(*args, **kwargs)


    def get(self, request, *args, **kwargs):
        if TipoDeEquipamento.objects.count() > 0:
            return super(TipoDeEquipamentoDetail, self).get(request, *args, **kwargs)
        else:
            return redirect(reverse('core:tipodeequipamento_add'))

class EquipamentoList(ListView):
    model = Equipamento

    def get(self, request, *args, **kwargs):
        if Equipamento.objects.count() > 0:
            return super(EquipamentoList, self).get(request, *args, **kwargs)
        else:
            return redirect(reverse('core:equipamento_add'))

    def dispatch(self, *args, **kwargs):
        return super(EquipamentoList, self).dispatch(*args, **kwargs)


class EquipamentoCreate(LoginMixin, CreateView):
    model = Equipamento
    success_url = '/equipamento/'
    fields = ['instalacao', 'tipo_de_equipamento', 'posicao_operacional']

    def dispatch(self, *args, **kwargs):
        return super(EquipamentoCreate, self).dispatch(*args, **kwargs)


class EquipamentoUpdate(LoginMixin, UpdateView):
    model = Equipamento
    success_url = '/equipamento/'
    fields = ['instalacao', 'tipo_de_equipamento', 'posicao_operacional']

    def dispatch(self, *args, **kwargs):
        return super(EquipamentoUpdate, self).dispatch(*args, **kwargs)


class EquipamentoDelete(LoginMixin, DeleteView):
    model = Equipamento
    success_url = '/equipamento/'

    def dispatch(self, *args, **kwargs):
        return super(EquipamentoDelete, self).dispatch(*args, **kwargs)


class FuncionarioList(ListView):
    model = Funcionario

    def get(self, request, *args, **kwargs):
        if Funcionario.objects.count() > 0:
            return super(FuncionarioList, self).get(request, *args, **kwargs)
        else:
            return redirect(reverse('core:funcionario_add'))

    def dispatch(self, *args, **kwargs):
        return super(FuncionarioList, self).dispatch(*args, **kwargs)


class FuncionarioCreate(LoginMixin, CreateView):
    model = Funcionario
    success_url = '/funcionario/'
    fields = ['equipe', 'usuario', 'nome']

    def dispatch(self, *args, **kwargs):
        return super(FuncionarioCreate, self).dispatch(*args, **kwargs)


class FuncionarioUpdate(LoginMixin, UpdateView):
    model = Funcionario
    success_url = '/funcionario/'
    fields = ['equipe', 'usuario', 'nome']

    def dispatch(self, *args, **kwargs):
        return super(FuncionarioUpdate, self).dispatch(*args, **kwargs)


class FuncionarioDelete(LoginMixin, DeleteView):
    model = Funcionario
    success_url = '/funcionario/'


class OSList(LoginMixin, ListView):
    model = OS

    def get(self, request, *args, **kwargs):
        if OS.objects.count() > 0:
            return super(OSList, self).get(request, *args, **kwargs)
        else:
            return redirect(reverse('core:os_add'))


class OSCreate(LoginMixin, CreateView):
    model = OS
    success_url = '/os/'
    fields = ['resumo_do_problema', 'descricao_detalhada', 'data_prevista', 'equipe_destinatario', 'equipamento_por_os']


    def form_valid(self, form):
        form.instance.usuario_criador = self.request.user
        return super(OSCreate, self).form_valid(form)

class OSCancelar(LoginMixin, UpdateView):
    model = OS
    success_url = '/os/'
    fields = ['status']

    def form_valid(self, form):
        form.instance.status = 'X'
        print('oi')
        return super(OSCancelar, self).form_valid(form)