# Базовый образ Python
FROM python:3.11

# Установка рабочей директории внутри контейнера
WORKDIR /code

# Скопировать файл зависимостей
COPY requirements.txt .

# Установить зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопировать весь проект внутрь контейнера
COPY . .