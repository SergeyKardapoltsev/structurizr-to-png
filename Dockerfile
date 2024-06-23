# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем Graphviz
RUN apt-get update && apt-get install -y graphviz

# Устанавливаем необходимые Python-библиотеки
RUN pip install graphviz

# Копируем наш скрипт в контейнер
COPY script.py /app/script.py

# Устанавливаем рабочую директорию
WORKDIR /app

# Указываем точку входа
ENTRYPOINT ["python", "script.py"]
