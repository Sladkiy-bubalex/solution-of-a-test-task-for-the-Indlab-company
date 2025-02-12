import os
import logging
from dotenv import load_dotenv
from fastapi.templating import Jinja2Templates


# Настройка шаблонов
templates = Jinja2Templates(directory="templates")

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Загрузка переменных окружения
load_dotenv()

# Ваша API информация (используйте переменные окружения для безопасности)
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
api_key_proxy_chatgpt = os.getenv("API_KEY_PROXY_CHATGPT")
