import sqlite3
import hashlib

# Função para criar a tabela de senhas no banco de dados
def criar_tabela_senhas():
    conn = sqlite3.connect("gerenciador_de_senhas.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS senhas (
        id INTEGER PRIMARY KEY,
        website TEXT,
        usuario TEXT,
        senha TEXT
    )
    """)
    conn.commit()
    conn.close()

# Função para adicionar uma nova senha ao banco de dados
def adicionar_senha(website, usuario, senha):
    conn = sqlite3.connect("gerenciador_de_senhas.db")
    cursor = conn.cursor()
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    cursor.execute("INSERT INTO senhas (website, usuario, senha) VALUES (?, ?, ?)", (website, usuario, senha_hash))
    conn.commit()
    conn.close()

# Função para listar todas as senhas do banco de dados
def listar_senhas():
    conn = sqlite3.connect("gerenciador_de_senhas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM senhas")
    senhas = cursor.fetchall()
    conn.close()
    return senhas

# Criar a tabela de senhas (se ainda não existir)
criar_tabela_senhas()

# Exemplo de uso:
# Adicionar novas senhas
adicionar_senha("example.com", "user123", "senha123")
adicionar_senha("outrosite.com", "alice", "senhasegura")

# Listar todas as senhas
senhas = listar_senhas()
print("Gerenciador de Senhas:")
for senha in senhas:
    print(f"Website: {senha[1]}, Usuário: {senha[2]}, Senha: {senha[3]}")
