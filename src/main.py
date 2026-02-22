
print('Hello from repository!')
from dotenv import load_dotenv
import os


def print_author():
    load_dotenv()  # загружает переменные из .env
    author = os.getenv("AUTHOR")  # читаем AUTHOR из .env
    print(f"Автор проекта: {author}")


print_author()
