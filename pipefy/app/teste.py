tasks = {
    '1025275652': 'Arrumar resposta do botão "Configurações"',
    '1034462005': 'Melhor Card',
    '1025275646': 'Arrumar bug da integração',
    '1025275651': 'Modificação na interface de login',
    '1025275647': 'Migração completa do servidor',
    '1025275648': 'Criar API de Pagamentos',
    '1025275649': 'Trabalhar na redução de fila no servidor',
    '1025275650': 'Alterar os gráficos da barra de progresso'
}

# Acessando valores pelo ID
task_id = '1025275652'
if task_id in tasks:
    print(f'Tarefa {task_id}: {tasks[task_id]}')

# Iterando sobre o dicionário
for task_id, description in tasks.items():
    print(f'ID: {task_id}, Descrição: {description}')

# Exemplo: Criar uma lista de todas as descrições
descriptions = list(tasks.values())
print(descriptions)

# Exemplo: Criar uma lista de todas as chaves
task_ids = list(tasks.keys())
print(task_ids)