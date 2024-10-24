from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Criar ou conectar ao banco de dados
conn = sqlite3.connect('registro_vacinacao.db')
cursor = conn.cursor()

# Criar tabela de vacinação se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS vacinacao (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_paciente TEXT NOT NULL,
        idade INTEGER,
        cpf TEXT UNIQUE,
        vacina TEXT,
        data_vacinacao TEXT
    )
''')

conn.commit()
conn.close()

# Rota principal para listar vacinações
@app.route('/')
def index():
    conn = sqlite3.connect('registro_vacinacao.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vacinacao')
    vacinacoes = cursor.fetchall()
    conn.close()
    return render_template('index.html', vacinacoes=vacinacoes)

# Rota para adicionar nova vacinação
@app.route('/nova_vacinacao', methods=['GET', 'POST'])
def nova_vacinacao():
    if request.method == 'POST':
        nome_paciente = request.form['nome_paciente']
        idade = request.form['idade']
        cpf = request.form['cpf']
        vacina = request.form['vacina']
        data_vacinacao = request.form['data_vacinacao']

        conn = sqlite3.connect('registro_vacinacao.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO vacinacao (nome_paciente, idade, cpf, vacina, data_vacinacao)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome_paciente, idade, cpf, vacina, data_vacinacao))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('nova_vacinacao.html')

if __name__ == '__main__':
    app.run(debug=True)
