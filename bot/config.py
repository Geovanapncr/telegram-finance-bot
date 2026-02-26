#Suas váriaveis de configuração devem ser feitas no arquivo .env
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
USER_ID = int(os.getenv("USER_ID"))
SALARIO = float(os.getenv("SALARIO"))
PORCENTAGEM_GUARDAR = float(os.getenv("PORCENTAGEM_GUARDAR"))