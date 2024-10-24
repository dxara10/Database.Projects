import sqlite3

# Função para criar a tabela de tarefas no banco de dados
def criar_tabela_tarefas():
    conn = sqlite3.connect("gerenciamento_de_tarefas.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY,
        titulo TEXT,
        descricao TEXT,
        responsavel TEXT,
        prazo DATE,
        concluida BOOLEAN
    )
    """)
    conn.commit()
    conn.close()

# Função para adicionar uma nova tarefa
def adicionar_tarefa(titulo, descricao, responsavel, prazo):
    conn = sqlite3.connect("gerenciamento_de_tarefas.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (titulo, descricao, responsavel, prazo, concluida) VALUES (?, ?, ?, ?, 0)",
                   (titulo, descricao, responsavel, prazo))
    conn.commit()
    conn.close()

# Função para listar tarefas por responsável
def listar_tarefas_por_responsavel(responsavel):
    conn = sqlite3.connect("gerenciamento_de_tarefas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas WHERE responsavel = ? ORDER BY prazo", (responsavel,))
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas

# Criar a tabela de tarefas (se ainda não existir)
criar_tabela_tarefas()

# Exemplo de uso:
# Adicionar tarefas
adicionar_tarefa("Projeto A", "Desenvolver funcionalidade X", "Alice", "2023-12-15")
adicionar_tarefa("Projeto B", "Testar funcionalidade Y", "Bob", "2023-12-16")

# Listar tarefas por responsável
tarefas_alice = listar_tarefas_por_responsavel("Alice")
tarefas_bob = listar_tarefas_por_responsavel("Bob")

print("Gerenciamento de Tarefas:")
print("Tarefas de Alice:")
for tarefa in tarefas_alice:
    print(f"Título: {tarefa[1]}, Descrição: {tarefa[2]}, Prazo: {tarefa[4]}")
print("Tarefas de Bob:")
for tarefa in tarefas_bob:
    print(f"Título: {tarefa[1]}, Descrição: {tarefa[2]}, Prazo: {tarefa[4]}")
