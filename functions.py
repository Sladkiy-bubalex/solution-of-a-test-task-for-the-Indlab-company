from openai import OpenAI
from config import api_id, api_hash, api_key_proxy_chatgpt, logger
from telethon.sessions import StringSession
from telethon import TelegramClient
from fastapi import Request


# Функция для суммаризации текста с учётом ограничений токенов
def summarize_text(text: str) -> str:
    try:
        client_openai = OpenAI(
            api_key=f"{api_key_proxy_chatgpt}",
            base_url="https://api.proxyapi.ru/openai/v1",
        )
        response = client_openai.chat.completions.create(
            model="gpt-4o",  # Используйте нужную модель
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that summarizes Telegram channel messages.",
                },
                {
                    "role": "user",
                    "content": f"Суммаризируй следующие сообщения:\n\n{text}",
                },
            ],
            max_tokens=4000,  # Ограничение на выходные токены
            temperature=1,
        )
        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        logger.error(f"Ошибка при суммаризации: {e}")
        return "Не удалось получить суммаризацию."
    

# Функция для получения текущего пользователя из сессии
async def get_current_user(request: Request):
    session_str = request.session.get("session_str")
    if not session_str:
        return None
    try:
        logger.debug(f"Session String in FastAPI: {session_str}")
        user_client = TelegramClient(StringSession(session_str), api_id, api_hash)
        await user_client.connect()
        if not await user_client.is_user_authorized():
            logger.warning("User is not authorized.")
            return None
    except Exception as e:
        logger.error(f"Authorization Error: {e}")
        return None


