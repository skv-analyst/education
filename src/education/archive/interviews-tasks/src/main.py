import sqlite3
import pandas as pd
import os

DB_PATH = "challenges.db"

def init_db():
    """Создает таблицы в БД, если их нет."""
    with sqlite3.connect(DB_PATH) as conn:
        with open("schema.sql", "r") as f:
            conn.executescript(f.read())

def add_challenge(company, position, grade, tags):
    """Добавляет новую запись в challenges."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO challenges (company, position, grade, tags) VALUES (?, ?, ?, ?)",
            (company, position, grade, tags)
        )

def add_question(challenge_id, question):
    """Добавляет новый вопрос к тестовому заданию."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO questions (challenge_id, question) VALUES (?, ?)",
            (challenge_id, question)
        )

def add_dataset(name, description, csv_path):
    """Создает SQL-таблицу для датасета и загружает данные из CSV."""
    conn = sqlite3.connect(DB_PATH)

    # Загружаем CSV в Pandas
    df = pd.read_csv(csv_path)

    # Сохраняем в SQL-таблицу
    df.to_sql(name, conn, if_exists="replace", index=False)

    # Добавляем запись в datasets
    with conn:
        conn.execute(
            "INSERT INTO datasets (name, description, csv_path) VALUES (?, ?, ?)",
            (name, description, csv_path)
        )

    conn.close()
    print(f"✅ Датасет '{name}' загружен в БД.")

if __name__ == "__main__":
    init_db()  # Создаем БД (если ее нет)

    # 1. Добавляем тестовое задание
    add_challenge("Google", "Data Analyst", "Middle", "SQL, Python")

    # 2. Добавляем вопросы
    add_question(1, "Напишите SQL-запрос для поиска самых активных пользователей.")
    add_question(1, "Как бы вы проанализировали аномалии в данных?")

    # 3. Загружаем датасет
    add_dataset("user_activity", "Лог активности пользователей", "../data/test1.csv")
