import telebot
import logging
import os
import json
import datetime
from typing import Optional

# Настройка логгера
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

# Инициализация бота
bot = telebot.TeleBot(os.environ.get("TG_BOT_TOKEN"), threaded=False)


def generate_response(message: telebot.types.Message) -> str:
    """Генерирует ответное сообщение с метаданными полученного контента."""
    response = ["✅ Данные получены\n"]
    
    # Обработка пересланных сообщений
    if message.forward_from_chat:
        chat = message.forward_from_chat
        response.extend([
            f"📲 Передано от: <code>{chat.title}</code>",
            f"🌐 ID: <code>{chat.id}</code>",
            f"📤 Тип: {'Публичный канал' if chat.username else 'Приватный'}"
        ])
        if chat.username:
            response.append(f"Ссылка: https://t.me/{chat.username}")
        response.append("")

    # Добавляем дату отправки
    response.append(f"📆 Дата отправки: <code>{datetime.datetime.fromtimestamp(message.date)}</code>\n")

    # Обработка разных типов контента
    content_handlers = {
        'photo': lambda: message.photo[-1],
        'video': lambda: message.video,
        'document': lambda: message.document
    }

    if message.content_type in content_handlers:
        file = content_handlers[message.content_type]()
        response.extend([
            f"🌐 {message.content_type.capitalize()} File ID: <code>{file.file_id}</code>",
            f"🌐 {message.content_type.capitalize()} Unique ID: <code>{file.file_unique_id}</code>"
        ])

    return "\n".join(response)


@bot.message_handler(commands=["start"])
def send_welcome(message: telebot.types.Message):
    """Обработчик команды /start"""
    bot.send_message(
        message.chat.id,
        "😎 Добрый день! Просто отправьте мне любое сообщение, файл, видео или текст, "
        "и я верну вам всю найденную информацию."
    )


@bot.message_handler(content_types=[
    'text', 'photo', 'video', 'document', 'sticker', 
    'location', 'voice', 'audio'
])
def handle_message(message: telebot.types.Message):
    """Основной обработчик входящих сообщений"""
    bot.send_message(
        message.chat.id,
        generate_response(message),
        parse_mode='HTML'
    )


def handler(event: dict, context) -> dict:
    """Обработчик для Yandex Cloud Functions"""
    try:
        update = telebot.types.Update.de_json(json.loads(event["body"]))
        if update.message:
            bot.process_new_updates([update])
    except Exception as e:
        logger.error(f"Error processing update: {e}")

    return {"statusCode": 200, "body": "ok"}
