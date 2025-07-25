# Telegram Metadata Bot 🤖

Бот для извлечения метаданных из сообщений Telegram (File ID, источник пересылки, дата отправки).  
**Разработан для Yandex Cloud Functions.**

![Telegram Bot Example](https://i.imgur.com/EXAMPLE.jpg) *(скриншот интерфейса, если есть)*

## 🔍 Возможности
- Получение `File ID` и `Unique ID` для:
  - Фото (`photo`)
  - Видео (`video`)
  - Документов (`document`)
- Информация о пересланных сообщениях:
  - Название чата/канала
  - Тип (публичный/приватный)
  - Ссылка (для публичных)
- Дата и время отправки сообщения

## 🛠 Технологии
- Python 3.10+
- Библиотека [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- Yandex Cloud Functions (Serverless)

## 🚀 Быстрый старт
### 1. Клонирование репозитория
```bash
git clone https://github.com/ваш-логин/telegram-bot.git
cd telegram-bot/projects/metadata-bot
