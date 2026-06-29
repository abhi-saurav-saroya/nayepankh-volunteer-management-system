from datetime import date

from database.database import insert_volunteer
from models.volunteers import Volunteer


class VolunteerService:

    def add_volunteer(self):
        print("\n=== Add New Volunteer ===")

        name = input("Name: ").strip()
        age = int(input("Age: "))
        gender = input("Gender: ").strip()
        phone = input("Phone: ").strip()
        email = input("Email: ").strip()
        city = input("City: ").strip()
        skill = input("Skill: ").strip()
        availability = input("Availability (Yes/No): ").strip()

        volunteer = Volunteer(
            id=None,
            name=name,
            age=age,
            gender=gender,
            phone=phone,
            email=email,
            city=city,
            skill=skill,
            availability=availability,
            join_date=str(date.today())
        )

        insert_volunteer(volunteer)

        print("\nVolunteer added successfully!")