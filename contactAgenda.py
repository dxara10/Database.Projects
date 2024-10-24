import sqlite3

# Função para criar a tabela de contatos no banco de dados
def criar_tabela_contatos():
    conn = sqlite3.connect("agenda_de_contatos.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        telefone TEXT,
        email TEXT
    )
    """)
    conn.commit()
    conn.close()

# Função para adicionar um novo contato ao banco de dados
def adicionar_contato(nome, telefone, email):
    conn = sqlite3.connect("agenda_de_contatos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))
    conn.commit()
    conn.close()

# Função para listar todos os contatos no banco de dados
def listar_contatos():
    conn = sqlite3.connect("agenda_de_contatos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()
    conn.close()
    return contatos

# Função para atualizar informações de um contato com base no ID
def atualizar_contato(id, nome, telefone, email):
    conn = sqlite3.connect("agenda_de_contatos.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE contatos SET nome = ?, telefone = ?, email = ? WHERE id = ?", (nome, telefone, email, id))
    conn.commit()
    conn.close()

# Criar a tabela de contatos (se ainda não existir)
criar_tabela_contatos()

# Exemplo de uso:
# Adicionar novos contatos
adicionar_contato("João", "123456789", "joao@email.com")
adicionar_contato("Maria", "987654321", "maria@email.com")

# Listar todos os contatos
contatos = listar_contatos()
print("Agenda de Contatos:")
for contato in contatos:
    print(f"ID: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}, Email: {contato[3]}")

# Atualizar as informações de um contato (por ID)
atualizar_contato(1, "João Silva", "987654321", "joao_silva@email.com")

# Listar os contatos atualizados
contatos = listar_contatos()
print("\nAgenda de Contatos Atualizada:")
for contato in contatos:
    print(f"ID: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}, Email: {contato[3]}")
