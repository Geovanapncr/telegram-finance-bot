#API do telegram - Cérebro
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters

#Agendador de tarefa sincronizado ao telegram
from apscheduler.schedulers.asyncio import AsyncIOScheduler

#funções do bot do arquivo handler
from .handlers import listar, apagar, mensagem, relatorio

#configurações de tolken e ID de usuário
from .config import TOKEN


def main():
    #builder pattern
    app = ApplicationBuilder().token(TOKEN).build()

    #texto E NÃO comando
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensagem))

    #execução de comandos (funções do handler)
    app.add_handler(CommandHandler("relatorio", relatorio))
    app.add_handler(CommandHandler("listar", listar))
    app.add_handler(CommandHandler("apagar", apagar))

    # scheduler só inicia depois do loop do telegram
    scheduler = AsyncIOScheduler()

    async def start_scheduler(app):
        scheduler.start()

    #depois que inicializar → rode essa função
    app.post_init = start_scheduler

    print("Bot rodando...")
    #rodagem do bot (cria loop sincronizado → conecta telegram → recebe mensagens → responde)
    app.run_polling()


if __name__ == "__main__":
    main()