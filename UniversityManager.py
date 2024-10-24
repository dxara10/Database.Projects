from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Criar ou conectar ao banco de dados
conn = sqlite3.connect('gerenciamento_alunos.db')
cursor = conn.cursor()

# Criar tabelas se não existirem
cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        matricula TEXT UNIQUE NOT NULL,
        curso TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS notas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER,
        disciplina TEXT NOT NULL,
        nota INTEGER NOT NULL,
        FOREIGN KEY (aluno_id) REFERENCES alunos (id)
    )
''')

conn.commit()
conn.close()

# Rota principal para listar alunos
@app.route('/')
def index():
    conn = sqlite3.connect('gerenciamento_alunos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alunos')
    alunos = cursor.fetchall()
    conn.close()
    return render_template('index.html', alunos=alunos)

# Rota para adicionar novo aluno
@app.route('/novo_aluno', methods=['GET', 'POST'])
def novo_aluno():
    if request.method == 'POST':
        nome = request.form['nome']
        matricula = request.form['matricula']
        curso = request.form['curso']

        conn = sqlite3.connect('gerenciamento_alunos.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO alunos (nome, matricula, curso) VALUES (?, ?, ?)', (nome, matricula, curso))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('novo_aluno.html')

# Rota para adicionar notas para um aluno
@app.route('/adicionar_nota/<int:aluno_id>', methods=['GET', 'POST'])
def adicionar_nota(aluno_id):
    if request.method == 'POST':
        disciplina = request.form['disciplina']
        nota = request.form['nota']

        conn = sqlite3.connect('gerenciamento_alunos.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO notas (aluno_id, disciplina, nota) VALUES (?, ?, ?)', (aluno_id, disciplina, nota))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('adicionar_nota.html', aluno_id=aluno_id)

if __name__ == '__main__':
    app.run(debug=True)
