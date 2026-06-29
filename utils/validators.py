import re


def get_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty.")


def get_positive_integer(prompt):
    while True:
        value = input(prompt).strip()

        try:
            number = int(value)

            if number > 0:
                return number

            print("Please enter a positive number.")

        except ValueError:
            print("Please enter a valid integer.")


def get_gender(prompt):
    valid_genders = ["Male", "Female", "Other"]

    while True:
        gender = input(prompt).strip().title()

        if gender in valid_genders:
            return gender

        print("Invalid gender. Choose Male, Female or Other.")


def get_phone(prompt):
    while True:
        phone = input(prompt).strip()

        if phone.isdigit() and len(phone) == 10:
            return phone

        print("Phone number must contain exactly 10 digits.")


def get_email(prompt):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    while True:
        email = input(prompt).strip()

        if re.fullmatch(pattern, email):
            return email

        print("Invalid email address.")


def get_availability(prompt):
    valid_options = ["Yes", "No"]

    while True:
        availability = input(prompt).strip().title()

        if availability in valid_options:
            return availability

        print("Enter either Yes or No.")