import requests
from decouple import config


def send_telegram_message(appointment):
    BOT_TOKEN = config('BOT_TOKEN')
    CHAT_ID = config('CHAT_ID')
    TEXT = (
        f"📥 Новая запись на приём:\n\n"
        f"👤 Имя: {appointment.name}\n"
        f"📧 Email: {appointment.email}\n"
        f"📞 Телефон: {appointment.phone}\n"
        f"📅 Дата: {appointment.date}\n"
        f"🏥 Отделение: {appointment.department}\n"
        f"💬 Сообщение: {appointment.message}\n\n"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': CHAT_ID, 'text': TEXT})
