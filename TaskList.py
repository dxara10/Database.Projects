import sqlite3

# Função para criar a tabela de tarefas no banco de dados
def criar_tabela_tarefas():
    conn = sqlite3.connect("lista_de_tarefas.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY,
        descricao TEXT,
        concluida BOOLEAN
    )
    """)
    conn.commit()
    conn.close()

# Função para adicionar uma nova tarefa ao banco de dados
def adicionar_tarefa(descricao):
    conn = sqlite3.connect("lista_de_tarefas.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (descricao, concluida) VALUES (?, ?)", (descricao, False))
    conn.commit()
    conn.close()

# Função para listar todas as tarefas no banco de dados
def listar_tarefas():
    conn = sqlite3.connect("lista_de_tarefas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas

# Função para marcar uma tarefa como concluída
def marcar_como_concluida(id):
    conn = sqlite3.connect("lista_de_tarefas.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tarefas SET concluida = ? WHERE id = ?", (True, id))
    conn.commit()
    conn.close()

# Função para remover uma tarefa do banco de dados
def remover_tarefa(id):
    conn = sqlite3.connect("lista_de_tarefas.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conn.commit()
    conn.close()

# Criar a tabela de tarefas (se ainda não existir)
criar_tabela_tarefas()

# Exemplo de uso:
# Adicionar novas tarefas
adicionar_tarefa("Fazer compras de supermercado")
adicionar_tarefa("Estudar para o exame")

# Listar todas as tarefas
tarefas = listar_tarefas()
print("Lista de Tarefas:")
for tarefa in tarefas:
    print(f"ID: {tarefa[0]}, Descrição: {tarefa[1]}, Concluída: {tarefa[2]}")

# Marcar uma tarefa como concluída (por ID)
marcar_como_concluida(1)

# Remover uma tarefa (por ID)
remover_tarefa(2)

# Listar as tarefas atualizadas
tarefas = listar_tarefas()
print("\nLista de Tarefas Atualizada:")
for tarefa in tarefas:
    print(f"ID: {tarefa[0]}, Descrição: {tarefa[1]}, Concluída: {tarefa[2]}")
