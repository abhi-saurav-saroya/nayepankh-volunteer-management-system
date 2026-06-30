import sqlite3
from models.volunteers import Volunteer

from utils.mapper import rows_to_volunteers

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


def get_all_volunteers():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            age,
            gender,
            phone,
            email,
            city,
            skill,
            availability,
            join_date
        FROM volunteers
        ORDER BY id
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows_to_volunteers(rows)


def search_volunteers(keyword: str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            age,
            gender,
            phone,
            email,
            city,
            skill,
            availability,
            join_date
        FROM volunteers
        WHERE
            name LIKE ?
            OR city LIKE ?
            OR skill LIKE ?
        ORDER BY id
    """, (
        f"%{keyword}%",
        f"%{keyword}%",
        f"%{keyword}%"
    ))

    rows = cursor.fetchall()
    connection.close()

    return rows_to_volunteers(rows)


def get_volunteer_by_id(volunteer_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            age,
            gender,
            phone,
            email,
            city,
            skill,
            availability,
            join_date
        FROM volunteers
        WHERE id = ?
    """, (volunteer_id,))

    row = cursor.fetchone()

    connection.close()

    if row:
        return Volunteer(*row)

    return None


def update_volunteer(volunteer: Volunteer):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE volunteers
        SET
            name = ?,
            age = ?,
            gender = ?,
            phone = ?,
            email = ?,
            city = ?,
            skill = ?,
            availability = ?,
            join_date = ?
        WHERE id = ?
    """, (
        volunteer.name,
        volunteer.age,
        volunteer.gender,
        volunteer.phone,
        volunteer.email,
        volunteer.city,
        volunteer.skill,
        volunteer.availability,
        volunteer.join_date,
        volunteer.id
    ))

    connection.commit()
    connection.close()


def delete_volunteer(volunteer_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM volunteers
        WHERE id = ?
    """, (volunteer_id,))

    connection.commit()
    connection.close()


def filter_volunteers(column: str, value: str):
    """
    Filter volunteers by a specific column and value.
    """

    allowed_columns = {
        "city",
        "skill",
        "availability"
    }

    if column not in allowed_columns:
        raise ValueError("Invalid filter column.")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(f"""
        SELECT
            id,
            name,
            age,
            gender,
            phone,
            email,
            city,
            skill,
            availability,
            join_date
        FROM volunteers
        WHERE {column} = ?
        ORDER BY id
    """, (value,))

    rows = cursor.fetchall()

    connection.close()

    return rows_to_volunteers(rows)


def get_total_volunteers():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM volunteers
    """)

    total = cursor.fetchone()[0]

    connection.close()
    return total


def get_available_volunteers_count():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM volunteers
        WHERE availability = 'Yes'
    """)

    total = cursor.fetchone()[0]

    connection.close()
    return total


def get_unavailable_volunteers_count():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM volunteers
        WHERE availability = 'No'
    """)

    total = cursor.fetchone()[0]

    connection.close()
    return total


def get_volunteers_by_city():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT city, COUNT(*)
        FROM volunteers
        GROUP BY city
        ORDER BY city
    """)

    rows = cursor.fetchall()

    connection.close()
    return rows


def get_volunteers_by_skill():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT skill, COUNT(*)
        FROM volunteers
        GROUP BY skill
        ORDER BY skill
    """)

    rows = cursor.fetchall()

    connection.close()
    return rows