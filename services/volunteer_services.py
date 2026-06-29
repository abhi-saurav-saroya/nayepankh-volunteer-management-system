from datetime import date

from database.database import insert_volunteer
from models.volunteers import Volunteer

from utils.validators import (
    get_text,
    get_positive_integer,
    get_gender,
    get_phone,
    get_email,
    get_availability
)


class VolunteerService:

    def add_volunteer(self):
        print("\n=== Add New Volunteer ===")

        name = get_text("Name: ")
        age = get_positive_integer("Age: ")
        gender = get_gender("Gender (Male/Female/Other): ")
        phone = get_phone("Phone: ")
        email = get_email("Email: ")
        city = get_text("City: ")
        skill = get_text("Skill: ")
        availability = get_availability("Availability (Yes/No): ")

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