from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Criando o banco de dados ou conectando a um já existente
conn = sqlite3.connect('agenda_medica.db')
cursor = conn.cursor()

# Criando a tabela de pacientes se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL
    )
''')

# Criando a tabela de agendamentos se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS agendamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER,
        data_hora TEXT NOT NULL,
        descricao TEXT,
        FOREIGN KEY (paciente_id) REFERENCES pacientes (id)
    )
''')
conn.commit()
conn.close()

# Rota principal para mostrar a lista de pacientes
@app.route('/')
def index():
    conn = sqlite3.connect('agenda_medica.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pacientes')
    pacientes = cursor.fetchall()
    conn.close()
    return render_template('index.html', pacientes=pacientes)

# Rota para adicionar um novo paciente
@app.route('/novo_paciente', methods=['GET', 'POST'])
def novo_paciente():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        
        conn = sqlite3.connect('agenda_medica.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO pacientes (nome, email, telefone) VALUES (?, ?, ?)', (nome, email, telefone))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('novo_paciente.html')

# Rota para visualizar os agendamentos de um paciente
@app.route('/agendamentos/<int:paciente_id>')
def agendamentos(paciente_id):
    conn = sqlite3.connect('agenda_medica.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM agendamentos WHERE paciente_id = ?', (paciente_id,))
    agendamentos = cursor.fetchall()
    cursor.execute('SELECT nome FROM pacientes WHERE id = ?', (paciente_id,))
    nome_paciente = cursor.fetchone()[0]
    conn.close()
    return render_template('agendamentos.html', agendamentos=agendamentos, nome_paciente=nome_paciente)

# Rota para agendar uma consulta para um paciente
@app.route('/agendar/<int:paciente_id>', methods=['GET', 'POST'])
def agendar(paciente_id):
    if request.method == 'POST':
        data_hora = request.form['data_hora']
        descricao = request.form['descricao']
        
        conn = sqlite3.connect('agenda_medica.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO agendamentos (paciente_id, data_hora, descricao) VALUES (?, ?, ?)', (paciente_id, data_hora, descricao))
        conn.commit()
        conn.close()
        return redirect(url_for('agendamentos', paciente_id=paciente_id))
    return render_template('agendar.html')

if __name__ == '__main__':
    app.run(debug=True)
