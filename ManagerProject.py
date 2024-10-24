import sqlite3

# Função para criar a tabela de projetos no banco de dados
def criar_tabela_projetos():
    conn = sqlite3.connect("gerenciamento_de_projetos.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projetos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        status TEXT
    )
    """)
    conn.commit()
    conn.close()

# Função para criar a tabela de tarefas no banco de dados
def criar_tabela_tarefas():
    conn = sqlite3.connect("gerenciamento_de_projetos.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY,
        projeto_id INTEGER,
        descricao TEXT,
        concluida BOOLEAN
    )
    """)
    conn.commit()
    conn.close()

# Função para adicionar um novo projeto
def adicionar_projeto(nome, status):
    conn = sqlite3.connect("gerenciamento_de_projetos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO projetos (nome, status) VALUES (?, ?)", (nome, status))
    conn.commit()
    conn.close()

# Função para adicionar uma nova tarefa a um projeto
def adicionar_tarefa(projeto_id, descricao):
    conn = sqlite3.connect("gerenciamento_de_projetos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (projeto_id, descricao, concluida) VALUES (?, ?, ?)", (projeto_id, descricao, False))
    conn.commit()
    conn.close()

# Função para listar todos os projetos
def listar_projetos():
    conn = sqlite3.connect("gerenciamento_de_projetos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projetos")
    projetos = cursor.fetchall()
    conn.close()
    return projetos

# Função para listar todas as tarefas de um projeto
def listar_tarefas(projeto_id):
    conn = sqlite3.connect("gerenciamento_de_projetos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas WHERE projeto_id = ?", (projeto_id,))
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas

# Criar as tabelas de projetos e tarefas (se ainda não existirem)
criar_tabela_projetos()
criar_tabela_tarefas()

# Exemplo de uso:
# Adicionar projetos e tarefas
adicionar_projeto("Projeto A", "Em andamento")
projeto_id = 1  # ID do projeto criado
adicionar_tarefa(projeto_id, "Desenvolver funcionalidade X")
adicionar_tarefa(projeto_id, "Testar funcionalidade X")

# Listar projetos e suas tarefas
projetos = listar_projetos()
print("Gerenciamento de Projetos:")
for projeto in projetos:
    print(f"ID: {projeto[0]}, Nome: {projeto[1]}, Status: {projeto[2]}")
    tarefas = listar_tarefas(projeto[0])
    for tarefa in tarefas:
        print(f"  Tarefa: {tarefa[2]}, Concluída: {tarefa[3]}")
