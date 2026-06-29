from datetime import date

from database.database import insert_volunteer, get_all_volunteers
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

    def view_all_volunteers(self):
        volunteers = get_all_volunteers()
    
        if not volunteers:
            print("\nNo volunteers found.")
            return
    
        print("\n" + "=" * 130)
    
        print(
            f"{'ID':<5}"
            f"{'Name':<20}"
            f"{'Age':<6}"
            f"{'Gender':<10}"
            f"{'Phone':<15}"
            f"{'City':<15}"
            f"{'Skill':<18}"
            f"{'Available':<12}"
            f"{'Join Date':<15}"
        )
    
        print("-" * 130)
    
        for volunteer in volunteers:
            print(
                f"{volunteer.id:<5}"
                f"{volunteer.name:<20}"
                f"{volunteer.age:<6}"
                f"{volunteer.gender:<10}"
                f"{volunteer.phone:<15}"
                f"{volunteer.city:<15}"
                f"{volunteer.skill:<18}"
                f"{volunteer.availability:<12}"
                f"{volunteer.join_date:<15}"
            )
    
        print("=" * 130)