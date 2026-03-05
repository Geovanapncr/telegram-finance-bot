# API do telegram - Cérebro
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters

# Agendador de tarefa sincronizado ao telegram
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# funções do bot do arquivo handler
from .handlers import listar, apagar, mensagem, relatorio

# configurações de token
from .config import TOKEN


def main():
    # builder pattern
    app = ApplicationBuilder().token(TOKEN).build()

    # texto E NÃO comando
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensagem))

    # execução de comandos
    app.add_handler(CommandHandler("relatorio", relatorio))
    app.add_handler(CommandHandler("listar", listar))
    app.add_handler(CommandHandler("apagar", apagar))

    # scheduler
    scheduler = AsyncIOScheduler()

    async def start_scheduler(app):
        # remove qualquer webhook antigo (evita conflito)
        await app.bot.delete_webhook(drop_pending_updates=True)
        scheduler.start()

    # executa após iniciar
    app.post_init = start_scheduler

    print("Bot rodando...")

    # polling mais seguro
    app.run_polling(
        drop_pending_updates=True
    )


if __name__ == "__main__":
    main()