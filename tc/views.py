from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import AutomatosForm, MaquinasForm, SequenciaForm
from .models import Automato, Maquina, Sequencia


# Create your views here.

def layout_view(request):
    return render(request, 'tc/base.html')


def intro_view(request):
    return render(request, 'tc/introducao.html')


def automatos_view(request):
    context = {'automatos': Automato.objects.all()}
    return render(request, 'tc/automatos.html', context)


def automatos_detalhes_view(request, automato_id):

    context = {
               'automato' : Automato.objects.get(pk=automato_id),
               'automato_id': automato_id
               }

    return render(request, 'tc/automatosdetalhes.html', context)


def automatos_form_view(request):
    form = AutomatosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tc:automatos'))

    context = {'form': form}
    return render(request, 'tc/automatosform.html', context)


def automatos_editar_view(request, automato_id):
    automato = Automato.objects.get(pk=automato_id)
    form = AutomatosForm(request.POST or None, instance=automato)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tc:automatos'))

    context = {'form': form,
               'automato_id': automato_id
               }

    return render(request, 'tc/automatoseditar.html', context)


def automatos_apagar_view(request, automato_id):
    Automato.objects.get(id=automato_id).delete()

    return HttpResponseRedirect(reverse('tc:automatos'))

def automatos_seq_view(request, automato_id):
    resultado = sequencia = None

    if request.POST:
        form = SequenciaForm(request.POST)  # a expressão submetida no formulário é guardada na variável form
        if form.is_valid():
            sequencia = form.cleaned_data['sequencia']
            try:
                for simbolo in sequencia:
                    estado_atual = Automato.tabela_transicao[(estado_atual, simbolo)]

                if estado_atual in Automato.estados_aceitacao:
                    resultado = eval(sequencia)
            except:
                resultado = "Sequencia Inválida"

    form = SequenciaForm(None)

    context = {
        'form': form,
        'resultado': resultado,
        'sequencia': sequencia
    }

    return render(request, 'tc/automatosseq.html', context)

def maquinas_view(request):
    context = {'maquinas': Maquina.objects.all()}
    return render(request, 'tc/maqturing.html', context)

def maquinas_detalhes_view(request, maquina_id):

    context = {
               'maquina' : Maquina.objects.get(pk=maquina_id),
               'maquina_id': maquina_id
               }

    return render(request, 'tc/maqturingdetalhes.html', context)

def maquinas_form_view(request):
    form = MaquinasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tc:maquinas'))

    context = {'form': form}
    return render(request, 'tc/maqturingform.html', context)

def maquinas_editar_view(request, maquina_id):
    maquina = Maquina.objects.get(pk=maquina_id)
    form = MaquinasForm(request.POST or None, instance=maquina)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tc:maquinas'))

    context = {'form': form,
               'maquina_id': maquina_id
               }

    return render(request, 'tc/maqturingeditar.html', context)

def maquinas_apagar_view(request, maquina_id):
    Maquina.objects.get(id=maquina_id).delete()

    return HttpResponseRedirect(reverse('tc:maquinas'))

def maquinas_seq_view(request, maquina_id):
    resultado = sequencia = None
    if request.POST:
        form = SequenciaForm(request.POST)  # a expressão submetida no formulário é guardada na variável form
        if form.is_valid():
            sequencia = form.cleaned_data['sequencia']
            try:
                for simbolo in sequencia:
                    estado_atual = Maquina.tabela_transicao[(estado_atual, simbolo)]

                if estado_atual in Maquina.halt_accept:
                    resultado = eval(sequencia)
            except:
                resultado = "Sequencia Inválida"

    form = SequenciaForm(None)

    context = {
        'form': form,
        'resultado': resultado,
        'sequencia': sequencia
    }

    return render(request, 'tc/maquinasseq.html', context)

