import sqlite3

class SistemaGestaoFornecedoresCompras:
    def __init__(self, nome_banco):
        self.conn = sqlite3.connect(nome_banco)
        self.criar_tabelas()
    
    def criar_tabelas(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fornecedores (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                contato TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS compras (
                id INTEGER PRIMARY KEY,
                fornecedor_id INTEGER,
                data_compra TEXT,
                valor REAL
            )
        ''')
        self.conn.commit()

    def adicionar_fornecedor(self, nome, contato):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO fornecedores (nome, contato) VALUES (?, ?)", (nome, contato))
        self.conn.commit()

    def listar_fornecedores(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nome FROM fornecedores")
        fornecedores = cursor.fetchall()
        return fornecedores

    def fazer_compra(self, fornecedor_id, data_compra, valor):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO compras (fornecedor_id, data_compra, valor) VALUES (?, ?, ?)", (fornecedor_id, data_compra, valor))
        self.conn.commit()

    def listar_compras(self, fornecedor_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT data_compra, valor FROM compras WHERE fornecedor_id=?", (fornecedor_id,))
        compras = cursor.fetchall()
        return compras

# Exemplo de uso:
sistema = SistemaGestaoFornecedoresCompras("fornecedores_compras.db")

# Adiciona fornecedores
sistema.adicionar_fornecedor("Fornecedor A", "Contato A")
sistema.adicionar_fornecedor("Fornecedor B", "Contato B")

# Lista fornecedores
fornecedores = sistema.listar_fornecedores()
print("Fornecedores:")
for fornecedor in fornecedores:
    print(f"ID: {fornecedor[0]}, Nome: {fornecedor[1]}")

# Realiza compras
sistema.fazer_compra(1, "2023-01-15", 1000.0)
sistema.fazer_compra(2, "2023-02-20", 1500.0)

# Lista compras para um fornecedor
compras_fornecedor_1 = sistema.listar_compras(1)
print("Compras para Fornecedor 1:")
for compra in compras_fornecedor_1:
    print(f"Data: {compra[0]}, Valor: {compra[1]}")
