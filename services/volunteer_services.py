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
    search_volunteers
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