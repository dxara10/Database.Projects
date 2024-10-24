import sqlite3

# Função para criar a tabela de reservas no banco de dados
def criar_tabela_reservas():
    conn = sqlite3.connect("sistema_de_reservas.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reservas (
        id INTEGER PRIMARY KEY,
        recurso TEXT,
        data_hora DATETIME,
        usuario TEXT
    )
    """)
    conn.commit()
    conn.close()

# Função para fazer uma reserva
def fazer_reserva(recurso, data_hora, usuario):
    conn = sqlite3.connect("sistema_de_reservas.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reservas (recurso, data_hora, usuario) VALUES (?, ?, ?)", (recurso, data_hora, usuario))
    conn.commit()
    conn.close()

# Função para listar todas as reservas
def listar_reservas():
    conn = sqlite3.connect("sistema_de_reservas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservas")
    reservas = cursor.fetchall()
    conn.close()
    return reservas

# Criar a tabela de reservas (se ainda não existir)
criar_tabela_reservas()

# Exemplo de uso:
# Fazer reservas
fazer_reserva("Sala de Reuniões 1", "2023-12-15 14:00", "Alice")
fazer_reserva("Laboratório de Computadores", "2023-12-16 10:30", "Bob")

# Listar todas as reservas
reservas = listar_reservas()
print("Sistema de Reservas:")
for reserva in reservas:
    print(f"Recurso: {reserva[1]}, Data e Hora: {reserva[2]}, Usuário: {reserva[3]}")
