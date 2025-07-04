from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Topico, Assunto

def index(request):
    logado = request.user.is_authenticated
    if logado:
        return redirect('indexLogin')
    user = 'Anonimo'

    if request.method == 'POST':
        nome_topico = request.POST.get('topico', '').strip()
        assunto_topico = request.POST.get('assunto', '').strip()
        
        if nome_topico and assunto_topico:
            topico, _ = Topico.objects.get_or_create(nome=nome_topico)
            Assunto.objects.create(topico=topico, texto=assunto_topico, usuario=user)

        return redirect('index')
    

    topicos = Topico.objects.all()
    topicos_assuntos = []

    for topico in topicos:
        assuntos = Assunto.objects.filter(topico=topico)
        topicos_assuntos.append({
            'topico': topico,
            'assuntos': assuntos
        })
    
    return render(request ,'index.html', {'topicos_assuntos': topicos_assuntos, 'usuario' : user})

def RegisterScreen(request):
    if request.method == 'POST':
        nome_register = request.POST.get('name', '').strip()
        sobrenome_register = request.POST.get('last-name', '').strip()
        email_register = request.POST.get('gmail', '').strip()
        usuario_register = request.POST.get('usuario').strip()
        senha_register = request.POST.get('senha', '').strip()
        
        if User.objects.filter(username=usuario_register):
            return HttpResponse("Usuario já existe")
        if User.objects.filter(email=email_register):
            return HttpResponse("Email Já cadastrado")
        
        User.objects.create_user(username=usuario_register, first_name=nome_register, last_name=sobrenome_register, email=email_register, password=senha_register)

        return redirect('index')
    
    return render(request, 'register.html')

def LoginScreen(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario', '').strip()
        senha = request.POST.get('senha', '').strip()

        user = authenticate(request, username=usuario, password=senha)
        
        if user is not None:
            login(request, user)
            return redirect('indexLogin')
        else:
            HttpResponse("Usuario ou senha incorretos")
    
    return render(request, 'login.html')

def indexLogin(request):
    logado = request.user.is_authenticated
    if logado != True:
        return HttpResponse("Você não esta logado, registre-se ou entre com sua conta")
    user = request.user
    if user:
        print(f"Autenticado como {user}")

    if request.method == 'POST':
        nome_topico = request.POST.get('topico', '').strip()
        assunto_topico = request.POST.get('assunto', '').strip()
        
        if nome_topico and assunto_topico:
            topico, _ = Topico.objects.get_or_create(nome=nome_topico)
            Assunto.objects.create(topico=topico, texto=assunto_topico, usuario=user)

        return redirect('index')
    

    topicos = Topico.objects.all()
    topicos_assuntos = []

    for topico in topicos:
        assuntos = Assunto.objects.filter(topico=topico)
        topicos_assuntos.append({
            'topico': topico,
            'assuntos': assuntos
        })
    
    return render(request ,'indexWithLogin.html', {'topicos_assuntos': topicos_assuntos, 'usuario' : user})

def deslogar(request):
    logout(request)
    return redirect('index')
    

