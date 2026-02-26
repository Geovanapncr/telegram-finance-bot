from datetime import date

#altere o vencimento do seu cartão aqui
vencimento = 7

def ciclo_atual(vencimento):
    hoje = date.today()

    #se hoje é menor igual a data do vencimento... ciclo atual se mantém
    if hoje.day <= vencimento:
        #mes = mes anterior
        mes = hoje.month - 1 or 12
        #ano = ajusta o ano se for janeiro (janeiro é mes anterior e mes anterior é dezembro do outro ano)
        ano = hoje.year if hoje.month > 1 else hoje.year - 1
        #quando começa o novo ciclo
        inicio = date(ano, mes, vencimento + 1)
        #dia do vencimento
        fim = date(hoje.year, hoje.month, vencimento)
    else:
        #fatura virada
        inicio = date(hoje.year, hoje.month, vencimento + 1)

        #tudo ao contrario, mes seguinte, ano seguinte (caso dezembro)
        mes = hoje.month + 1 if hoje.month < 12 else 1
        ano = hoje.year if hoje.month < 12 else hoje.year + 1
        #vencimento do próximo mês
        fim = date(ano, mes, vencimento)

    #retorna datas formatadas
    return inicio.isoformat(), fim.isoformat()