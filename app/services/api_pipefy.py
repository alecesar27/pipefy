import requests, os
import json
# from integration.access import HEADERS,url
from integration.access import HEADERS, url


def create_pipe(organization_id,name):
    # Definindo a consulta GraphQL 
    mutation = """
    mutation {
      createPipe(input: {organization_id: %d , name:"%s"}) {
        clientMutationId
      }
    }
    """ % (organization_id,name )

    # Enviando a solicitação
    response = requests.post(url, json={'query': mutation}, headers=HEADERS)

    # Verificando a resposta
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro na solicitação: {response.status_code}, {response.text}")
    

def update_pipe(pipe_id, name):
    # Definindo a consulta GraphQL
    mutation = """
    mutation {
      updatePipe(input: {id: %d, name: "%s"}) {
        pipe {
          id
        }
      }
    }
    """ % (pipe_id, name)
    # Enviando a solicitação
    response = requests.post(url, json={'query': mutation}, headers=HEADERS)

    # Verificando a resposta
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro na solicitação: {response.status_code}, {response.text}")

def delete_pipe(pipe_id):
    # Definindo a consulta GraphQL
    mutation = """
    mutation {
      deletePipe(input: {id: %d}) {
        success
      }
    }
    """ % pipe_id

    # Enviando a solicitação
    response = requests.post(url, json={'query': mutation}, headers=HEADERS)

    # Verificando a resposta
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro na solicitação: {response.status_code}, {response.text}")
    
def get_pipe_reports(pipe_id: int):
    # Definindo a consulta GraphQL
    query = f"""
    {{
      pipe(id: {pipe_id}) {{
        reports {{
          id
          name
        }}
      }}
    }}
    """

    # Enviando a solicitação
    response = requests.post(url, json={'query': query}, headers=HEADERS)

    # Verificando a resposta
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(status_code=response.status_code, detail=f"Erro na solicitação: {response.status_code}, {response.text}")
    

def export_pipe_report(pipe_id: int, pipe_report_id: int):
    # Definindo a mutação GraphQL
    mutation = f"""
    mutation {{
      exportPipeReport(input: {{
        pipeId: {pipe_id}, 
        pipeReportId: {pipe_report_id}
      }}) {{
        pipeReportExport {{
          id
        }}
      }}
    }}
    """

    # Enviando a solicitação
    response = requests.post(url, json={'query': mutation}, headers=HEADERS)

    # Verificando a resposta
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(status_code=response.status_code, detail=f"Erro na solicitação: {response.status_code}, {response.text}")



def create_phase(pipe_id: str, color:str, name: str):
    # Definindo a mutação GraphQL
    mutation = f"""
    mutation {{
      createPhase(input: {{ pipe_id: "{pipe_id}", color: "{color}", name: "{name}" }}) {{
        phase {{
          id
        }}
      }}
    }}
    """

    # Enviando a solicitação
    response = requests.post(url, json={'query': mutation}, headers=HEADERS)

    # Verificando a resposta
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(status_code=response.status_code, detail=f"Erro na solicitação: {response.status_code}, {response.text}")

def update_phase(phase_id: str, color: str, name: str):
    # Definindo a mutação GraphQL
    mutation = f"""
    mutation {{
      updatePhase(input: {{ id: {phase_id}, color: "{color}", name: "{name}" }}) {{
        phase {{
          id
        }}
      }}
    }}
    """

    # Enviando a solicitação
    response = requests.post(url, json={'query': mutation}, headers=HEADERS)

    # Verificando a resposta
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(status_code=response.status_code, detail=f"Erro na solicitação: {response.status_code}, {response.text}")

def delete_phase(phase_id: int):
    # Definindo a mutação GraphQL
    mutation = f"""
    mutation {{
      deletePhase(input: {{ id: {phase_id} }}) {{
        clientMutationId
        success
      }}
    }}
    """

    # Enviando a solicitação
    response = requests.post(url, json={'query': mutation}, headers=HEADERS)

    # Verificando a resposta
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(status_code=response.status_code, detail=f"Erro na solicitação: {response.status_code}, {response.text}")


def get_phase(phase_id: int):
    # Definindo a consulta GraphQL
    query = f"""
    {{
      phase(id: {phase_id}) {{
        id
        name
      }}
    }}
    """

    # Enviando a solicitação
    response = requests.post(url, json={'query': query}, headers=HEADERS)

    # Verificando a resposta
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(status_code=response.status_code, detail=f"Erro na solicitação: {response.status_code}, {response.text}")
    
def create_phase_field(phase_id: int, label: str, field_type: str, options: list):
    # Definindo a mutação GraphQL
    options_string = '", "'.join(options)  # Formata a lista de opções para a string correta
    mutation = f"""
    mutation {{
      createPhaseField(input: {{
        phase_id: {phase_id}, 
        label: "{label}", 
        type: "{field_type}", 
        options: ["{options_string}"]
      }}) {{
        phase_field {{
          id
          label
        }}
      }}
    }}
    """

    # Enviando a solicitação
    response = requests.post(url, json={'query': mutation}, headers=HEADERS)

    # Verificando a resposta
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(status_code=response.status_code, detail=f"Erro na solicitação: {response.status_code}, {response.text}") 
    
def update_phase_field(field_id: str, label: str, required: bool):
    # Definindo a mutação GraphQL
    mutation = f"""
    mutation {{
      updatePhaseField(input: {{
        id: "{field_id}", 
        label: "{label}", 
        required: {str(required).lower()}
      }}) {{
        phase_field {{
          label
          id
        }}
      }}
    }}
    """

    # Enviando a solicitação
    response = requests.post(url, json={'query': mutation}, headers=HEADERS)

    # Verificando a resposta
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(status_code=response.status_code, detail=f"Erro na solicitação: {response.status_code}, {response.text}")


def delete_phase_field(pipe_uuid: str, field_id: str):
    # Definindo a mutação GraphQL
    mutation = f"""
    mutation {{
      deletePhaseField(input: {{
        pipeUuid: "{pipe_uuid}", 
        id: "{field_id}"
      }}) {{
        success
      }}
    }}
    """

    # Enviando a solicitação
    response = requests.post(url, json={'query': mutation}, headers=HEADERS)

    # Verificando a resposta
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(status_code=response.status_code, detail=f"Erro na solicitação: {response.status_code}, {response.text}")

def list_pipes():
    # Definindo a consulta GraphQL
    query = """
      {
        organizations{
           id
           name
           pipes{
             color
             icon
             id
             name
             
           }
          
        }
      }
    """ 
    response = requests.post(url, json={'query': query}, headers=HEADERS)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(status_code=response.status_code, detail=f"Erro na solicitação: {response.status_code}, {response.text}")
    
def list_pipes_complete():
    # Definindo a consulta GraphQL
    query = """
      {
        organizations{
           id
           name
           pipes{
              color
              icon
              id
              name
              phases{
                 id
                 name 
                 
              } 

           }          
        }
      }
    """ 
    response = requests.post(url, json={'query': query}, headers=HEADERS)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(status_code=response.status_code, detail=f"Erro na solicitação: {response.status_code}, {response.text}")

def get_organization():
    # Definindo a consulta GraphQL
    query = """
      {
        organizations{                               
             id
             name          
        }
      }
    """ 
    response = requests.post(url, json={'query': query}, headers=HEADERS)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(status_code=response.status_code, detail=f"Erro na solicitação: {response.status_code}, {response.text}")  

def get_all_cards(pipe_id):
    all_cards={}
    payload = f'{{"query":"{{ allCards (pipeId:{pipe_id}, first:50) {{ edges {{ node {{ id title fields {{ name report_value updated_at value }} }} }} }} }}"}}'
    response = requests.request("POST", url, data=payload, headers=HEADERS)
    dic = json.loads(response.text)

    #print(dic)
    #Acessando os dados
    for card in dic['data']['allCards']['edges']:
      #print(card['node']['id'], card['node']['title'])
      all_cards[card['node']['id']] = card['node']['title']  # Atualiza o dicionário corretamente

    return all_cards

def get_all_card_details(pipe_id):
    all_cards = {}
    payload = f'{{"query":"{{ allCards (pipeId:{pipe_id}, first:50) {{ edges {{ node {{ id title fields {{ name report_value updated_at value }} }} }} }} }}"}}'
    response = requests.request("POST", url, data=payload, headers=HEADERS)
    dic = json.loads(response.text)
    print(dic)
    for card in dic['data']['allCards']['edges']:
        # Extrai as informações desejadas
        card_id = card['node']['id']
        card_title = card['node']['title']
        card_fields = card['node']['fields']
       
        # Adiciona as informações ao dicionário
        all_cards[card_id] = {
            'title': card_title,
            'fields': card_fields
        }

    return all_cards  # Retorna o dicionário com todos os cartões

def get_card_details(pipe_id,id_card):
    card_details = {}
    payload = f'{{"query":"{{ allCards (pipeId:{pipe_id}, first:50) {{ edges {{ node {{ id title fields {{ name report_value updated_at value }} }} }} }} }}"}}'
    response = requests.request("POST", url, data=payload, headers=HEADERS)
    dic = json.loads(response.text)

    for card in dic['data']['allCards']['edges']:
        # Extrai as informações desejadas
        if id_card == card['node']['id']:
          card_id = card['node']['id']
          card_title = card['node']['title']
          card_fields = card['node']['fields']

          # Adiciona as informações ao dicionário
          card_details[card_id] = {
              'title': card_title,
              'fields': card_fields
          }

    return card_details  # Retorna o dicionário com todos os cartões


def get_card_details_phase(pipe_id,id_card):
    card_details = {}
    payload = f'{{"query":"{{ allCards (pipeId:{pipe_id}, first:50) {{ edges {{ node {{ id title  phases_history{{ phase{{ id name }}  }}   fields {{ name report_value updated_at value    }}   }} }} }} }}"}}'

    response = requests.request("POST", url, data=payload, headers=HEADERS)
    dic = json.loads(response.text)

    for card in dic['data']['allCards']['edges']:
        # Extrai as informações desejadas
        if id_card == card['node']['id']:
          card_id = card['node']['id']
          card_title = card['node']['title']
          card_fields = card['node']['fields']

          # Adiciona as informações ao dicionário
          card_details[card_id] = {
              'title': card_title,
              'fields': card_fields
          }

    return card_details  # Retorna o dicionário com todos os cartões


# Função para criar um card
def create_card(pipe_id, title):
    mutation = f'''
    mutation {{
      createCard(input: {{
        pipe_id: "{pipe_id}",
        title: "{title}"
      }}) {{
        card {{
          id
          title
        }}
      }}
    }}
    '''
    response = requests.post(url, json={'query': mutation}, headers=HEADERS)
    return response.json()

# Função para atualizar um card
def update_title_card(card_id, title=None):
    mutation = f'''
    mutation {{
      updateCard(input: {{
        id: "{card_id}",
        title: {f'"{title}"' if title else 'null'}
      }}) {{
        card {{
          id
          title
        }}
      }}
    }}
    '''
    response = requests.post(url, json={'query': mutation}, headers=HEADERS)
    return response.json()
# Função para deletar um card
def delete_card(card_id):
    mutation = f'''
    mutation {{
      deleteCard(input: {{
        id: "{card_id}"
      }}) {{
        success
      }}
    }}
    '''
    response = requests.post(url, json={'query': mutation}, headers=HEADERS)
    return response.json()

#print(create_pipe('Melhor Pipe do Mundo',301424863))
#print(update_pipe(305487792, 'Melhor Pipe do Mundo Dobrado'))
#print(delete_pipe(305487792))
#print(get_all_cards(305087031))
#ids=['305087790']
#print(list_pipes(url,ids))
#print(get_card_details_phase(305087031,'1025275646'))
#print(get_organization())
#print(list_organizations())
#print(get_card_details(305087031,'1025275646'))
#print(list_pipes())

# pipe_id = 305087031  # Substitua pelo ID do seu pipe
# novo_card = create_card(pipe_id, 'Criar Tela de Login')
# print("Novo Card:", novo_card)
#id_card='1029774496'
# updated_card = update_title_card(id_card,'Criar a Tela de Login X')
# print(updated_card)
#print(delete_card(id_card))

