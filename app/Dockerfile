# Используем официальный образ Python
FROM python:3.9-slim
# Устанавливаем рабочую директорию
WORKDIR /app
# Копируем файл зависимостей
COPY ../requirements.txt .
# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt
# Копируем остальной код приложения
COPY . .
# Указываем переменные окружения
ENV PYTHONUNBUFFERED 1
# Открываем порт, который будет использоваться приложением
EXPOSE 8000
# Определяем команду для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

