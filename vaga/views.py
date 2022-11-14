from django.shortcuts import render
from django.http import Http404
from empresa.models import Vaga
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render,redirect,get_object_or_404
from models import Tarefa

def nova_vaga(request):
    if request.method=='POST':
        titulo = request.POST.get('titulo')
        email = request.POST.get('email')
        tecnologias_domina = request.POST.getlist('tecnologias_domina')
        tecnologias_nao_domina = request.POST.getlist('tecnologias_nao_domina')
        experiencia = request.POST.get('experiencia')
        data_final = request.POST.get('data_final')
        empresa = request.POST.get('empresa')
        status = request.POST.get('status')

        # TODO: validations

        vaga = Vaga(
            titulo=titulo,
            email=email,
            nivel_experiencia=experiencia,
            data_final=data_final,
            empresa_id=empresa,
            status=status,
        )


        vaga.save()

        vaga.tecnologias_estudar.add(*tecnologias_nao_domina)
        vaga.tecnologias_dominadas.add(*tecnologias_domina)

        vaga.save()
        messages.add_message(request, constants.SUCCESS, 'Vaga criada com sucesso.')
        
        return redirect(f'/empresa/{empresa}')
    
    elif request.method=='GET':
        raise Http404()
    
    return render(request, 'vaga/nova_vaga.html')

def vaga(request,id):
    vaga=get_object_or_404(Vaga,id=id)
    
    context={
        'vaga':vaga
    }
    return render(request,'vaga.html',context=context)

def nova_tarefa(request,id_vaga):
    titulo = request.POST.get('titulo')
    prioridade = request.POST.get("prioridade")
    data = request.POST.get('data')
    
    tarefa = Tarefa(vaga_id=id_vaga,
                    titulo=titulo,
                    prioridade=prioridade,
                    data=data)
    tarefa.save()
    messages.add_message(request, constants.SUCCESS, 'Tarefa criada com sucesso')
    return redirect(f'/vagas/vaga/{id_vaga}')
