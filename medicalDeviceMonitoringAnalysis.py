import random
import time
import sqlite3

# Criar ou conectar ao banco de dados
conn = sqlite3.connect('dados_dispositivos.db')
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS dados_dispositivos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp INTEGER,
        batimentos INTEGER,
        pressao_sistolica INTEGER,
        pressao_diastolica INTEGER
    )
''')
conn.commit()
conn.close()

# Simulação de coleta de dados de dispositivos médicos
def coletar_dados_simulados():
    conn = sqlite3.connect('dados_dispositivos.db')
    cursor = conn.cursor()

    while True:
        # Simular valores de batimentos cardíacos, pressão sistólica e diastólica
        batimentos = random.randint(60, 100)
        pressao_sistolica = random.randint(100, 140)
        pressao_diastolica = random.randint(60, 90)
        timestamp = int(time.time())

        # Inserir dados no banco de dados
        cursor.execute('''
            INSERT INTO dados_dispositivos (timestamp, batimentos, pressao_sistolica, pressao_diastolica)
            VALUES (?, ?, ?, ?)
        ''', (timestamp, batimentos, pressao_sistolica, pressao_diastolica))
        conn.commit()

        time.sleep(2)  # Espera 2 segundos antes de coletar o próximo conjunto de dados

# Iniciar a coleta de dados simulados
coletar_dados_simulados()
