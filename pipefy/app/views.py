from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import requests
from .forms import SignUpForm,  LoginForm, CreatePipeForm, UpdatePipeForm, CreatePhaseForm, CreateCardForm,UpdateCardForm


BASE_API_URL = 'http://localhost:8080'

@login_required
def home(request):

    return list_pipes(request)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Define a senha
            user.save()
            messages.success(request, 'Conta criada com sucesso! Você pode fazer login agora.')
            return redirect('login')  # Redireciona para a página de login
        else:
            messages.error(request, "As senhas não são iguais ou usuário já existente!")
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, "Login realizado com sucesso!")
                return redirect('home')  # Redirecione para a página inicial ou outra página
            else:
                messages.error(request, "Credenciais inválidas.")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    auth_logout(request)  # Faz o logout do usuário
    return redirect('login')  # Redireciona para a página de login após logout

@login_required
def get_organizations(request):
    try:
        response = requests.get(f'{BASE_API_URL}/organization/')
        if response.status_code == 200:
            data = response.json()
            organization_id = data.get('data', {}).get('organizations', ['id'])
            print(organization_id)
            return render(request, 'base.html', {'organization_id': organization_id})
        else:
            return HttpResponse(f"Falha ao recuperar organizações. Código de Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Ocorreu um erro: {str(e)}")

@login_required
def list_pipes(request):
    try:
        # Chamada para a API FastAPI para obter a lista de organizações
        response = requests.get(f'{BASE_API_URL}/list-pipes/')
               
        if response.status_code == 200:
            # Supondo que a resposta seja um dicionário
            data = response.json()
            
            # Verifique se a estrutura da resposta é a esperada
            if isinstance(data, dict) and 'data' in data and 'organizations' in data['data']:
                organizations = data['data']['organizations']
                return render(request, 'index.html', {
                    'organizations': organizations,
                    'organization_id': organizations[0]['id'] if organizations else None

                    })
            else:
                return HttpResponse("Formato de resposta inválido. Esperado um dicionário com chave 'data'.")
        else:
            return HttpResponse(f"Falha ao recuperar organizações. Código de Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Ocorreu um erro: {str(e)}")

@login_required
def create_pipe(request,organization_id):
    if request.method == 'POST':
        form = CreatePipeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']            
            
            response = requests.post(f'{BASE_API_URL}/create-pipe/?organization_id={organization_id}&name={name}')
            
            if response.status_code == 200:
                return HttpResponse("Pipe created successfully.")
            else:                
                return HttpResponse("Failed to create pipe.")
    else:
        form = CreatePipeForm()
    
    return render(request, 'create_pipe.html', {'form': form})

@login_required
def update_pipe(request, pipe_id):
    if request.method == 'POST':
        form = UpdatePipeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            response = requests.put(f'{BASE_API_URL}/update-pipe/{pipe_id}?name={name}')
            
            if response.status_code == 200:
                return HttpResponse("Pipe updated successfully.")
            else:
                return HttpResponse(f"Failed to update pipe. Status Code: {response.status_code}")
    else:
        form = UpdatePipeForm(initial={'name': ''})  # Inicializa o formulário, se necessário

    return render(request, 'update_pipe.html', {'form': form, 'pipe_id': pipe_id})

@login_required
def delete_pipe(request, pipe_id):
    if request.method == 'POST':
        # Se a requisição for POST, tenta excluir o pipe
        response = requests.delete(f'{BASE_API_URL}/delete-pipe/{pipe_id}/')
        if response.status_code == 204:  # Código de sucesso para exclusão
            messages.success(request, "Pipe excluído com sucesso.")
            return redirect('home')  # Redireciona para a página inicial ou lista de pipes
        else:
            messages.error(request, f"Falha ao excluir pipe. Código de Status: {response.status_code}")
            return redirect('home')  # Redireciona em caso de falha

    # Se a requisição não for POST, renderiza uma página de confirmação
    return render(request, 'home')

@login_required
def create_phase(request):
    if request.method == 'POST':
        form = CreatePhaseForm(request.POST)
        if form.is_valid():
            pipe_id = form.cleaned_data['pipe_id']
            name = form.cleaned_data['name']
            response = requests.post(f'{BASE_API_URL}/create-phase', json={'pipe_id': pipe_id, 'name': name})
            if response.status_code == 200:
                return HttpResponse("Phase created successfully.")
            else:
                return HttpResponse("Failed to create phase.")
    else:
        form = CreatePhaseForm()
    return render(request, 'create_phase.html', {'form': form})

@login_required
def create_card(request,pipe_id):
    if request.method == 'POST':
        form = CreateCardForm(request.POST)
        if form.is_valid():

            title = form.cleaned_data['title']
            response = requests.post(f'{BASE_API_URL}/create-card/?pipe_id={pipe_id}&title={title}')
            if response.status_code == 200:
                return HttpResponse("Card created successfully.")
            else:
                return HttpResponse("Failed to create card.")
    else:
        form = CreateCardForm()
    return render(request, 'create_card.html', {'form': form})

@login_required
def read_cards(request, pipe_id):
    try:
        if request.method == 'GET':
            # Chamada para a API para obter os cards do pipe específico
            response = requests.get(f'{BASE_API_URL}/cards/{pipe_id}')
            
            if response.status_code == 200:
                # Supondo que a resposta seja uma lista de cards
                cards = response.json()
                
                # Verifique se a estrutura da resposta é a esperada
                if isinstance(cards, dict):
               
                    return render(request, 'cards.html', {'cards': cards, 'pipe_id': pipe_id})  # Renderizando o template com os cards
                else:
                    return HttpResponse("Formato de resposta inválido. Esperado uma lista de cards.")
            else:
                return HttpResponse(f"Falha ao recuperar cards. Código de Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Ocorreu um erro: {str(e)}")
    
@login_required
def read_card_details(request, pipe_id, id_card):
    try:
        # Chamada para a API para obter os detalhes do cartão
        response = requests.get(f'{BASE_API_URL}/card-details/{pipe_id}/{id_card}')
        
        if response.status_code == 200:
            # Supondo que a resposta seja um dicionário com os detalhes do cartão
            card_details = response.json()

            return render(request, 'card_details.html', {'card_details': card_details})  # Renderizando o template com os detalhes do cartão
        else:
            return HttpResponse(f"Falha ao recuperar detalhes do cartão. Código de Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Ocorreu um erro: {str(e)}")
    
@login_required
def update_card_title(request, card_id):
    if request.method == 'POST':
        form = UpdateCardForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']

            response = requests.put(f'{BASE_API_URL}/update-card-title/{card_id}?title={title}')

            if response.status_code == 200:
                return HttpResponse("Card title updated successfully.")
                #return render(request, 'home' )
            else:
                return HttpResponse("Failed to update card title.")
    else:
        
        form = UpdateCardForm(initial={'title': ''})  # Inicializa o formulário, se necessário

    return render(request, 'update_card.html', {'form': form, 'card_id': card_id})

@login_required
def delete_card(request, card_id):
    if request.method == 'POST':
        try:
            response = requests.delete(f'{BASE_API_URL}/delete-card/{card_id}')
            if response.status_code == 200:
                messages.success(request, "Card deleted successfully.")
            else:
                messages.error(request, f"Failed to delete card. Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            messages.error(request, f"Ocorreu um erro: {str(e)}")
        
        return redirect('home')  # Redireciona para a página inicial ou outra página após a exclusão

    # Se não for um POST, você pode renderizar uma página de confirmação, se desejar
    return render(request, 'home')


         

