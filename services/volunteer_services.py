from datetime import date

from models.volunteers import Volunteer
from utils.table_formatter import print_volunteers

from utils.validators import (
    get_text,
    get_positive_integer,
    get_gender,
    get_phone,
    get_email,
    get_availability
)

from database.database import (
    insert_volunteer,
    get_all_volunteers,
    search_volunteers,
    get_volunteer_by_id,
    update_volunteer
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
        print_volunteers(volunteers)

    def search_volunteer(self):
        print("\n=== Search Volunteer ===")
        keyword = get_text("Enter name, city or skill: ")

        volunteers = search_volunteers(keyword)
        print_volunteers(volunteers)

    def update_volunteer(self):
        print("\n=== Update Volunteer ===")

        volunteer_id = get_positive_integer("Enter Volunteer ID: ")

        volunteer = get_volunteer_by_id(volunteer_id)

        if volunteer is None:
            print("\nVolunteer not found.")
            return

        print("\nPress Enter to keep the current value.\n")

        name = get_text(
            f"Name [{volunteer.name}]: ",
            allow_empty=True
        )
        if name is not None:
            volunteer.name = name

        age = get_positive_integer(
            f"Age [{volunteer.age}]: ",
            allow_empty=True
        )
        if age is not None:
            volunteer.age = age

        gender = get_gender(
            f"Gender [{volunteer.gender}]: ",
            allow_empty=True
        )
        if gender is not None:
            volunteer.gender = gender

        phone = get_phone(
            f"Phone [{volunteer.phone}]: ",
            allow_empty=True
        )
        if phone is not None:
            volunteer.phone = phone

        email = get_email(
            f"Email [{volunteer.email}]: ",
            allow_empty=True
        )
        if email is not None:
            volunteer.email = email

        city = get_text(
            f"City [{volunteer.city}]: ",
            allow_empty=True
        )
        if city is not None:
            volunteer.city = city

        skill = get_text(
            f"Skill [{volunteer.skill}]: ",
            allow_empty=True
        )
        if skill is not None:
            volunteer.skill = skill

        availability = get_availability(
            f"Availability [{volunteer.availability}]: ",
            allow_empty=True
        )
        if availability is not None:
            volunteer.availability = availability

        update_volunteer(volunteer)

        print("\nVolunteer updated successfully!")