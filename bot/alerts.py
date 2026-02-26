
from .database import total_mes
from .config import SALARIO, PORCENTAGEM_GUARDAR

def verificar_alerta():
    gasto = total_mes()
    limite = SALARIO * (1 - PORCENTAGEM_GUARDAR/100)

    if gasto >= limite:
        return "⚠️ Você entrou no vermelho!"
    elif gasto >= limite * 0.8:
        return "⚠️ Atenção: você está perto do limite!"
    return None

def status_financeiro(total, limite):
    if total >= limite:
        return "🔴 Você estourou o limite do ciclo."
    elif total >= limite * 0.8:
        return "🟡 Atenção: 80% do limite usado."
    return None