# Используем официальный образ Python
FROM python:3.12-slim
RUN groupadd -r groupdjango && useradd -r -g groupdjango userdj

# Устанавливаем переменную среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
# Устанавливаем рабочую директорию
WORKDIR /app/www/aclinic
# Копируем зависимости
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

USER userdj


