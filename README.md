Esse é um projeto que cria uma api integrando com o Pipefy para isso foi utilizado a linguagem Python e o framework FastApi no backend integrado com a Graphql do Pipefy. No frontend
foi criado um projeto usando o Django framewoerk.Foi adotado uma arquitetura baseada em SOLID em camadas. Após  o download sugere-se criar um ambiente virtualizado e fazer as 
instalações dos pacotes necessários. Seguir os passos


1-Instalar o python
https://www.python.org/downloads/

2- Criar um ambiente virtualizado para cada projeto
  - após baixar o projeto acessar a pasta app que está o backend e instalar o ambiente virtualizado rodando o comando:
  - python3 -m venv nome_do_ambiente
  - executar o ambiente virtualizado
  - executar pip install -r requirements.txt
3- acessar a pasta do frontend pipefy
   - instalar o ambiente virtualizado
   - python3 -m venv nome_do_ambient
   - executar pip install -r requirements.txt

4- rodar cada ambiente virtualizado
entrar na pasta \app mesma pasta em que esta o arquivo main.py e executar o comando:
- uvicorn main:app --host 127.0.0.1  --port 80 (mudar para a sua porta preferida)

5- entrar na pasta pipefy que é o frontend 
    - na mesma pasta em que está o arquivo manage.py executar o comando:
    python .\manage.py runserver


6-no backend acessar a pasta app\integration\access.py e colocar o token gerado no portal do pipefy para que você possa acessar os seus pipes e cartões 
no portal https://app.pipefy.com/


