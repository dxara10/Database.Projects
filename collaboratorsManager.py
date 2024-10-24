import sqlite3

# Conectar ao banco de dados SQLite (será criado se não existir)
conn = sqlite3.connect('gerenciamento_de_funcionarios.db')

# Criar a tabela de funcionários
conn.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        cargo TEXT,
        salario REAL,
        historico TEXT
    )
''')

# Função para adicionar um novo funcionário
def adicionar_funcionario(nome, cargo, salario, historico):
    conn.execute('INSERT INTO funcionarios (nome, cargo, salario, historico) VALUES (?, ?, ?, ?)', (nome, cargo, salario, historico))
    conn.commit()

# Função para listar todos os funcionários
def listar_funcionarios():
    cursor = conn.execute('SELECT id, nome FROM funcionarios')
    for row in cursor:
        print(f'ID: {row[0]}, Nome: {row[1]}')

# Função para exibir os detalhes de um funcionário específico
def mostrar_funcionario(id):
    cursor = conn.execute('SELECT nome, cargo, salario, historico FROM funcionarios WHERE id = ?', (id,))
    row = cursor.fetchone()
    if row:
        print(f'Nome: {row[0]}\nCargo: {row[1]}\nSalário: {row[2]}\nHistórico: {row[3]}')
    else:
        print('Funcionário não encontrado.')

# Exemplo de uso:
adicionar_funcionario('Maria', 'Engenheira de Software', 75000.0, 'Experiência em desenvolvimento web.')
adicionar_funcionario('João', 'Analista de Marketing', 55000.0, 'Especializado em estratégias de marketing digital.')
listar_funcionarios()
mostrar_funcionario(1)

# Fechar a conexão com o banco de dados quando terminar
conn.close()
