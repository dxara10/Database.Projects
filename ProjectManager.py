import sqlite3

class SistemaGestaoProjetosTarefas:
    def __init__(self, nome_banco):
        self.conn = sqlite3.connect(nome_banco)
        self.criar_tabelas()

    def criar_tabelas(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS projetos (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                descricao TEXT,
                data_inicio TEXT,
                data_prazo TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY,
                projeto_id INTEGER,
                descricao TEXT,
                data_prazo TEXT,
                concluida INTEGER
            )
        ''')
        self.conn.commit()

    def criar_projeto(self, nome, descricao, data_inicio, data_prazo):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO projetos (nome, descricao, data_inicio, data_prazo) VALUES (?, ?, ?, ?)",
                       (nome, descricao, data_inicio, data_prazo))
        self.conn.commit()

    def criar_tarefa(self, projeto_id, descricao, data_prazo):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO tarefas (projeto_id, descricao, data_prazo, concluida) VALUES (?, ?, ?, 0)",
                       (projeto_id, descricao, data_prazo))
        self.conn.commit()

    def listar_projetos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nome FROM projetos")
        projetos = cursor.fetchall()
        return projetos

    def listar_tarefas(self, projeto_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, descricao, data_prazo, concluida FROM tarefas WHERE projeto_id=?", (projeto_id,))
        tarefas = cursor.fetchall()
        return tarefas

    def marcar_tarefa_concluida(self, tarefa_id):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE tarefas SET concluida=1 WHERE id=?", (tarefa_id,))
        self.conn.commit()

# Exemplo de uso:
sistema = SistemaGestaoProjetosTarefas("gestao_projetos_tarefas.db")

# Cria um projeto
sistema.criar_projeto("Projeto A", "Descrição do Projeto A", "2023-01-01", "2023-02-28")

# Cria tarefas para o projeto
projeto_id = 1
sistema.criar_tarefa(projeto_id, "Tarefa 1", "2023-02-10")
sistema.criar_tarefa(projeto_id, "Tarefa 2", "2023-02-15")

# Lista projetos
projetos = sistema.listar_projetos()
print("Projetos:")
for projeto in projetos:
    print(f"ID: {projeto[0]}, Nome: {projeto[1]}")

# Lista tarefas para o projeto
tarefas_projeto = sistema.listar_tarefas(projeto_id)
print(f"Tarefas para Projeto {projeto_id}:")
for tarefa in tarefas_projeto:
    concluida = "Concluída" if tarefa[3] == 1 else "Pendente"
    print(f"ID: {tarefa[0]}, Descrição: {tarefa[1]}, Prazo: {tarefa[2]}, Status: {concluida}")

# Marca uma tarefa como concluída
tarefa_id = 1
sistema.marcar_tarefa_concluida(tarefa_id)

# Lista tarefas novamente para verificar a conclusão
tarefas_projeto = sistema.listar_tarefas(projeto_id)
print(f"Tarefas para Projeto {projeto_id} (após marcação de conclusão):")
for tarefa in tarefas_projeto:
    concluida = "Concluída" if tarefa[3] == 1 else "Pendente"
    print(f"ID: {tarefa[0]}, Descrição: {tarefa[1]}, Prazo: {tarefa[2]}, Status: {concluida}")
