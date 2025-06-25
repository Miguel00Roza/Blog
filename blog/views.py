from django.shortcuts import render, redirect
from .models import Topico, Assunto

def index(request):
    if request.method == 'POST':
        nome_topico = request.POST.get('topico', '').strip()
        assunto_topico = request.POST.get('assunto', '').strip()
        
        if nome_topico and assunto_topico:
            topico, _ = Topico.objects.get_or_create(nome=nome_topico)
            Assunto.objects.create(topico=topico, texto=assunto_topico)

        return redirect('index')
    

    topicos = Topico.objects.all()
    topicos_assuntos = []

    for topico in topicos:
        assuntos = Assunto.objects.filter(topico=topico)
        topicos_assuntos.append({
            'topico': topico,
            'assuntos': assuntos
        })
    return render(request ,'index.html', {'topicos_assuntos': topicos_assuntos})
