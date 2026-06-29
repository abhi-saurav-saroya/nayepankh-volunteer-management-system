from models.volunteers import Volunteer


def rows_to_volunteers(rows):
    volunteers = []

    for row in rows:
        volunteers.append(
            Volunteer(
                id=row[0],
                name=row[1],
                age=row[2],
                gender=row[3],
                phone=row[4],
                email=row[5],
                city=row[6],
                skill=row[7],
                availability=row[8],
                join_date=row[9]
            )
        )

    return volunteers