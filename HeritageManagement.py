import sqlite3

# Conectar ao banco de dados SQLite (será criado se não existir)
conn = sqlite3.connect('gestao_de_patrimonio.db')

# Criar a tabela de ativos
conn.execute('''
    CREATE TABLE IF NOT EXISTS ativos (
        id INTEGER PRIMARY KEY,
        tipo TEXT,
        descricao TEXT,
        valor REAL
    )
''')

# Função para adicionar um novo ativo
def adicionar_ativo(tipo, descricao, valor):
    conn.execute('INSERT INTO ativos (tipo, descricao, valor) VALUES (?, ?, ?)', (tipo, descricao, valor))
    conn.commit()

# Função para listar todos os ativos
def listar_ativos():
    cursor = conn.execute('SELECT id, tipo, descricao, valor FROM ativos')
    for row in cursor:
        print(f'ID: {row[0]}, Tipo: {row[1]}, Descrição: {row[2]}, Valor: R$ {row[3]:.2f}')

# Exemplo de uso:
adicionar_ativo('Imóvel', 'Casa própria', 250000.0)
adicionar_ativo('Investimento', 'Ações da Empresa XYZ', 5000.0)
listar_ativos()

# Fechar a conexão com o banco de dados quando terminar
conn.close()
