from .database import total_mes
from .config import SALARIO, PORCENTAGEM_GUARDAR

def gerar_relatorio():
    gasto = total_mes()
    guardado = SALARIO * (PORCENTAGEM_GUARDAR/100)
    saldo = SALARIO - gasto - guardado

    return f"""
📊 RELATÓRIO MENSAL

Salário: {SALARIO}
Total gasto: {gasto}
Guardado: {guardado}
Saldo restante: {saldo}
"""