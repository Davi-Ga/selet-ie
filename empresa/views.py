from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Tecnologia,Empresa,Vaga
from django.contrib import messages
from django.contrib.messages import constants
from . import models

def nova_empresa(request):
    if request.method=='GET':
        tecs=Tecnologia.objects.all()
    elif request.method=='POST':
        nome=request.POST.get('nome')
        email=request.POST.get('email')
        cidade=request.POST.get('cidade')
        endereco=request.POST.get('endereco')
        nicho=request.POST.get('nicho')
        caracteristicas=request.POST.get('caractetisticas')
        tecnologias=request.POST.getlist('tecnologias')
        logo=request.FILES.get('logo')

        if nicho not in [i[0] for i in models.CHOICES_NICHO]:
            messages.add_message(request, constants.ERROR, 'Nicho de mercado inválido')
            return redirect('/nova_empresa')
        
        empresa = Empresa(
            logo=logo,
            nome=nome,
            email=email,
            cidade=cidade,
            endereco=endereco,
            nicho=nicho,
            caracteristicas=caracteristicas,
        )
        empresa.save()
        empresa.tecnologias.add(*tecnologias)
        empresa.save()
        messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com sucesso')
        
        return redirect('/empresas')
    context={
            'tecs':tecs,

        }
    return render(request,'nova_empresa.html',context=context)

def empresas(request):
    tecnologias_filtrar=request.GET.get('tecnologias')  
    nome_filtrar=request.GET.get('nome')    
    empresas=Empresa.objects.all()
    
    if tecnologias_filtrar:
        empresas=empresas.filter(tecnologias=tecnologias_filtrar)
    
    if nome_filtrar:
        empresas=empresas.filter(nome__icontains=nome_filtrar)
    
    tecnologias=Tecnologia.objects.all()
    context={
        'empresas':empresas,
        'tecnologias':tecnologias
    }
    
    return render(request,'empresas.html',context=context)

def empresa(request,id):
    empresa=get_object_or_404(Empresa,id=id)
    tecnologias=Tecnologia.objects.all()
    empresas=Empresa.objects.all()
    vagas=Vaga.objects.filter(empresa_id=id)
    context={
        'empresa':empresa,
        'tecnologias':tecnologias,
        'empresas':empresas,
        'vagas':vagas
    }
    return render(request,'empresa.html',context=context)

def excluir_empresa(request, id):
    empresa = Empresa.objects.get(id=id)
    empresa.delete()
    messages.add_message(request, constants.SUCCESS, 'Empresa excluída com sucesso')
    
    return redirect('/empresas')