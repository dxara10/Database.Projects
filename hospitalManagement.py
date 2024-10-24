from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Criando ou conectando ao banco de dados
conn = sqlite3.connect('gestao_hospitalar.db')
cursor = conn.cursor()

# Criando tabelas se não existirem
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        sexo TEXT,
        cpf TEXT UNIQUE,
        endereco TEXT,
        telefone TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS consultas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER,
        data_hora TEXT,
        descricao TEXT,
        FOREIGN KEY (paciente_id) REFERENCES pacientes (id)
    )
''')

conn.commit()
conn.close()

# Rota principal para listar pacientes
@app.route('/')
def index():
    conn = sqlite3.connect('gestao_hospitalar.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pacientes')
    pacientes = cursor.fetchall()
    conn.close()
    return render_template('index.html', pacientes=pacientes)

# Rota para adicionar novo paciente
@app.route('/novo_paciente', methods=['GET', 'POST'])
def novo_paciente():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        sexo = request.form['sexo']
        cpf = request.form['cpf']
        endereco = request.form['endereco']
        telefone = request.form['telefone']

        conn = sqlite3.connect('gestao_hospitalar.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO pacientes (nome, idade, sexo, cpf, endereco, telefone)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nome, idade, sexo, cpf, endereco, telefone))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('novo_paciente.html')

# Rota para listar consultas de um paciente específico
@app.route('/consultas/<int:paciente_id>')
def consultas(paciente_id):
    conn = sqlite3.connect('gestao_hospitalar.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM consultas WHERE paciente_id = ?', (paciente_id,))
    consultas = cursor.fetchall()
    cursor.execute('SELECT nome FROM pacientes WHERE id = ?', (paciente_id,))
    nome_paciente = cursor.fetchone()[0]
    conn.close()
    return render_template('consultas.html', consultas=consultas, nome_paciente=nome_paciente)

# Rota para agendar uma consulta para um paciente
@app.route('/agendar/<int:paciente_id>', methods=['GET', 'POST'])
def agendar(paciente_id):
    if request.method == 'POST':
        data_hora = request.form['data_hora']
        descricao = request.form['descricao']

        conn = sqlite3.connect('gestao_hospitalar.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO consultas (paciente_id, data_hora, descricao)
            VALUES (?, ?, ?)
        ''', (paciente_id, data_hora, descricao))
        conn.commit()
        conn.close()
        return redirect(url_for('consultas', paciente_id=paciente_id))
    return render_template('agendar.html')

if __name__ == '__main__':
    app.run(debug=True)
