from django.shortcuts import render, redirect, get_object_or_404
from .models import CadastroPlantas

def criar_planta(request):
    if request.method == 'POST':
        CadastroPlantas.objects.create(
            nome=request.POST.get('nome'),
            nomeCientifico=request.POST.get('nomeCientifico'),
            descricao=request.POST.get('descricao'),
            regiao=request.POST.get('regiao'),
        )
        return redirect('criar_plantas')

    plantas = CadastroPlantas.objects.all()
    return render(request, 'criar_plantas.html', {'plantas': plantas})


def deletar_planta(request, id):
    planta = get_object_or_404(CadastroPlantas, id=id)
    planta.delete()
    return redirect('criar_plantas')


def atualizar_planta(request, id):
    planta = get_object_or_404(CadastroPlantas, id=id)

    if request.method == 'POST':
        planta.nome = request.POST.get('nome')
        planta.nomeCientifico = request.POST.get('nomeCientifico')
        planta.descricao = request.POST.get('descricao')
        planta.regiao = request.POST.get('regiao')
        planta.save()
        return redirect('criar_plantas')

    return render(request, 'atualizar_planta.html', {'planta': planta})
