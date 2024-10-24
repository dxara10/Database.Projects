import sqlite3

# Conectar ao banco de dados SQLite (será criado se não existir)
conn = sqlite3.connect('livro_de_receitas.db')

# Criar a tabela de receitas
conn.execute('''
    CREATE TABLE IF NOT EXISTS receitas (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        ingredientes TEXT,
        instrucoes TEXT
    )
''')

# Função para adicionar uma nova receita
def adicionar_receita(nome, ingredientes, instrucoes):
    conn.execute('INSERT INTO receitas (nome, ingredientes, instrucoes) VALUES (?, ?, ?)', (nome, ingredientes, instrucoes))
    conn.commit()

# Função para listar todas as receitas
def listar_receitas():
    cursor = conn.execute('SELECT id, nome FROM receitas')
    for row in cursor:
        print(f'ID: {row[0]}, Nome: {row[1]}')

# Função para exibir os detalhes de uma receita específica
def mostrar_receita(id):
    cursor = conn.execute('SELECT nome, ingredientes, instrucoes FROM receitas WHERE id = ?', (id,))
    row = cursor.fetchone()
    if row:
        print(f'Nome: {row[0]}\nIngredientes: {row[1]}\nInstruções: {row[2]}')
    else:
        print('Receita não encontrada.')

# Exemplo de uso:
adicionar_receita('Bolo de Chocolate', 'Farinha, açúcar, cacau em pó', 'Misture tudo e asse.')
listar_receitas()
mostrar_receita(1)

# Fechar a conexão com o banco de dados quando terminar
conn.close()
