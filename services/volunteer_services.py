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
    
        volunteer.name = self._update_field("Name", volunteer.name)
    
        age = input(f"Age [{volunteer.age}]: ").strip()
        if age:
            volunteer.age = int(age)
    
        volunteer.gender = self._update_field("Gender", volunteer.gender)
    
        volunteer.phone = self._update_field("Phone", volunteer.phone)
    
        volunteer.email = self._update_field("Email", volunteer.email)
    
        volunteer.city = self._update_field("City", volunteer.city)
    
        volunteer.skill = self._update_field("Skill", volunteer.skill)
    
        volunteer.availability = self._update_field(
            "Availability",
            volunteer.availability
        )
    
        update_volunteer(volunteer)
    
        print("\nVolunteer updated successfully.")

    @staticmethod
    def _update_field(prompt, current_value):
        value = input(f"{prompt} [{current_value}]: ").strip()

        if value == "":
            return current_value

        return value