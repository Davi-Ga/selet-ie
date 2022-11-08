from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tecnologia,Empresa
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

        if logo.size > 100_000_000:
            messages.add_message(request, constants.ERROR, 'A logo da empresa deve ter menos de 10MB')
            return redirect('/nova_empresa')

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
            caracteristicas=caracteristicas
        )
        empresa.save()
        empresa.tecnologias.add(*tecnologias)
        empresa.save()
        messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com sucesso')
        
        return redirect('/empresas')
    context={
            'tecs':tecs
        }
    return render(request,'nova_empresa.html',context=context)

def empresas(request):
    empresas=Empresa.objects.all()
    context={
        'empresas':empresas,
    }
    
    return render(request,'empresas.html',context=context)

def excluir_empresa(request, id):
    empresa = Empresa.objects.get(id=id)
    empresa.delete()
    messages.add_message(request, constants.SUCCESS, 'Empresa excluída com sucesso')
    
    return redirect('/empresas')