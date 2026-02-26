import re
from telegram import Update
from telegram.ext import ContextTypes
from .database import add_gasto
from .alerts import verificar_alerta
from .reports import gerar_relatorio

async def mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    match = re.search(r"(\d+\.?\d*)\s*(\w+)", texto)

    if match:
        valor = float(match.group(1))
        categoria = match.group(2)

        add_gasto(valor, categoria)
        alerta = verificar_alerta()

        resposta = f"✅ Gasto registrado: {valor} em {categoria}"

        if alerta:
            resposta += f"\n{alerta}"

        await update.message.reply_text(resposta)

async def relatorio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(gerar_relatorio())

from telegram import Update
from telegram.ext import ContextTypes
from .database import listar_gastos, apagar_gasto


async def listar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    gastos = listar_gastos()

    if not gastos:
        await update.message.reply_text("Nenhum gasto cadastrado.")
        return

    texto = "Seus gastos:\n\n"
    for g in gastos:
        texto += f"ID {g[0]} | R$ {g[1]:.2f} | {g[2]} | {g[3]}\n"

    texto += "\nPara apagar: /apagar ID"

    await update.message.reply_text(texto)


async def apagar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Use: /apagar ID")
        return

    try:
        gasto_id = int(context.args[0])
        apagar_gasto(gasto_id)
        await update.message.reply_text("Gasto apagado com sucesso.")
    except:
        await update.message.reply_text("ID inválido.")