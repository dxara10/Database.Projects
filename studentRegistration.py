import sqlite3

# Função para criar a tabela de alunos no banco de dados
def criar_tabela_alunos():
    conn = sqlite3.connect("cadastro_alunos.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER,
        notas REAL
    )
    """)
    conn.commit()
    conn.close()

# Função para adicionar um novo aluno ao banco de dados
def adicionar_aluno(nome, idade, notas):
    conn = sqlite3.connect("cadastro_alunos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alunos (nome, idade, notas) VALUES (?, ?, ?)", (nome, idade, notas))
    conn.commit()
    conn.close()

# Função para listar todos os alunos no banco de dados
def listar_alunos():
    conn = sqlite3.connect("cadastro_alunos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    conn.close()
    return alunos

# Função para atualizar informações de um aluno com base no ID
def atualizar_aluno(id, nome, idade, notas):
    conn = sqlite3.connect("cadastro_alunos.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE alunos SET nome = ?, idade = ?, notas = ? WHERE id = ?", (nome, idade, notas, id))
    conn.commit()
    conn.close()

# Criar a tabela de alunos (se ainda não existir)
criar_tabela_alunos()

# Exemplo de uso:
# Adicionar um novo aluno
adicionar_aluno("João", 20, 9.5)
adicionar_aluno("Maria", 22, 8.7)

# Listar todos os alunos
alunos = listar_alunos()
print("Lista de Alunos:")
for aluno in alunos:
    print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Idade: {aluno[2]}, Notas: {aluno[3]}")

# Atualizar as informações de um aluno (por ID)
atualizar_aluno(1, "João Silva", 21, 9.8)

# Listar os alunos atualizados
alunos = listar_alunos()
print("\nLista de Alunos Atualizada:")
for aluno in alunos:
    print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Idade: {aluno[2]}, Notas: {aluno[3]}")
