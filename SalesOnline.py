import sqlite3

# Função para criar as tabelas de produtos e vendas no banco de dados
def criar_tabela_produtos():
    conn = sqlite3.connect("sistema_de_vendas.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        preco REAL,
        estoque INTEGER
    )
    """)
    conn.commit()
    conn.close()

def criar_tabela_vendas():
    conn = sqlite3.connect("sistema_de_vendas.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY,
        produto_id INTEGER,
        quantidade INTEGER,
        data DATE
    )
    """)
    conn.commit()
    conn.close()

# Função para adicionar um novo produto
def adicionar_produto(nome, preco, estoque):
    conn = sqlite3.connect("sistema_de_vendas.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)", (nome, preco, estoque))
    conn.commit()
    conn.close()

# Função para realizar uma venda
def realizar_venda(produto_id, quantidade, data):
    conn = sqlite3.connect("sistema_de_vendas.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vendas (produto_id, quantidade, data) VALUES (?, ?, ?)", (produto_id, quantidade, data))
    conn.commit()
    conn.close()

# Função para calcular o total de vendas
def calcular_total_vendas():
    conn = sqlite3.connect("sistema_de_vendas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(p.preco * v.quantidade) FROM produtos p JOIN vendas v ON p.id = v.produto_id")
    total_vendas = cursor.fetchone()[0]
    conn.close()
    return total_vendas

# Criar as tabelas de produtos e vendas (se ainda não existirem)
criar_tabela_produtos()
criar_tabela_vendas()

# Exemplo de uso:
# Adicionar produtos
adicionar_produto("Produto A", 10.0, 100)
adicionar_produto("Produto B", 15.0, 50)

# Realizar vendas
realizar_venda(1, 5, "2023-12-15")
realizar_venda(2, 3, "2023-12-16")

# Calcular o total de vendas
total_vendas = calcular_total_vendas()

print("Sistema de Vendas Online:")
print(f"Total de Vendas: R${total_vendas:.2f}")
