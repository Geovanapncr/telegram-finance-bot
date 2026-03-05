from .database import total_mes
from .config import SALARIO, PORCENTAGEM_GUARDAR

def gerar_relatorio():
    gasto = total_mes()
    guardado = SALARIO * (PORCENTAGEM_GUARDAR/100)
    saldo = SALARIO - gasto - guardado

    return f"""
📊 RELATÓRIO MENSAL

Salário: {SALARIO:.2f}
Total gasto: {gasto:.2f}
Guardado: {guardado:.2f}
Saldo restante: {saldo:.2f}
"""
