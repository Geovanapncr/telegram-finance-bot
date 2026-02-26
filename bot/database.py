#Funções de Manipulação do Database
import sqlite3
from .utils import ciclo_atual


# ---------------- CONEXÃO ----------------
conn = sqlite3.connect("financeiro.db", check_same_thread=False)
cursor = conn.cursor()


# ---------------- CRIAÇÃO DAS TABELAS ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS gastos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    valor REAL NOT NULL,
    categoria TEXT,
    data DATE DEFAULT CURRENT_DATE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS entradas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    valor REAL NOT NULL,
    categoria TEXT,
    data DATE DEFAULT CURRENT_DATE
)
""")

conn.commit()


# ---------------- ADICIONAR GASTO ----------------
def add_gasto(valor, categoria):
    cursor.execute(
        "INSERT INTO gastos (valor, categoria) VALUES (?, ?)",
        (valor, categoria)
    )
    conn.commit()


# ---------------- ADICIONAR ENTRADA ----------------
def add_entrada(valor, categoria):
    cursor.execute(
        "INSERT INTO entradas (valor, categoria) VALUES (?, ?)",
        (valor, categoria)
    )
    conn.commit()


# ---------------- TOTAL GASTOS DO CICLO ----------------
def total_gastos_ciclo():
    inicio, fim = ciclo_atual()

    cursor.execute("""
        SELECT SUM(valor)
        FROM gastos
        WHERE data BETWEEN ? AND ?
    """, (inicio, fim))

    r = cursor.fetchone()[0]
    return r if r else 0


# ---------------- TOTAL ENTRADAS DO CICLO ----------------
def total_entradas_ciclo():
    inicio, fim = ciclo_atual()

    cursor.execute("""
        SELECT SUM(valor)
        FROM entradas
        WHERE data BETWEEN ? AND ?
    """, (inicio, fim))

    r = cursor.fetchone()[0]
    return r if r else 0


# ---------------- SALDO DO CICLO ----------------
def saldo_ciclo():
    entradas = total_entradas_ciclo()
    gastos = total_gastos_ciclo()
    return entradas - gastos

def total_mes():
    cursor.execute("""
        SELECT SUM(valor)
        FROM gastos
        WHERE strftime('%Y-%m', data) = strftime('%Y-%m', 'now')
    """)
    r = cursor.fetchone()[0]
    return r if r else 0

def listar_gastos():
    cursor.execute("""
        SELECT id, valor, categoria, data
        FROM gastos
        ORDER BY data DESC
    """)
    return cursor.fetchall()

def apagar_gasto(gasto_id):
    cursor.execute("""
        DELETE FROM gastos
        WHERE id = ?
    """, (gasto_id,))
    conn.commit()