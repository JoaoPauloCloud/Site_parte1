from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages
from app1.models import Aluno

# Create your views here.
def index(request):
    alunos = Aluno.objects.all()

    testChave = {

        'alunos': alunos

    }

    return render(request, 'index.html', testChave)

def aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    context = {
        'aluno': aluno
    }
    return render(request, 'aluno.html', context)