import requests


def send_telegram_message(appointment):
    BOT_TOKEN = '7561986373:AAHxKMyS5tR8-N-EDqsrp1Q_jEpQKTPfF60'  # Замени на свой токен
    CHAT_ID = '430326400'  # Замени на свой ID
    TEXT = (
        f"📥 Новая запись на приём:\n\n"
        f"👤 Имя: {appointment.name}\n"
        f"📧 Email: {appointment.email}\n"
        f"📞 Телефон: {appointment.phone}\n"
        f"📅 Дата: {appointment.date}\n"
        f"💬 Сообщение: {appointment.message}"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': CHAT_ID, 'text': TEXT})