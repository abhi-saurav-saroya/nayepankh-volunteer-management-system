import sqlite3
from models.volunteers import Volunteer

DATABASE_NAME = "database/volunteers.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS volunteers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            city TEXT NOT NULL,
            skill TEXT NOT NULL,
            availability TEXT NOT NULL,
            join_date TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def insert_volunteer(volunteer: Volunteer):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO volunteers (
            name,
            age,
            gender,
            phone,
            email,
            city,
            skill,
            availability,
            join_date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        volunteer.name,
        volunteer.age,
        volunteer.gender,
        volunteer.phone,
        volunteer.email,
        volunteer.city,
        volunteer.skill,
        volunteer.availability,
        volunteer.join_date
    ))

    connection.commit()
    connection.close()