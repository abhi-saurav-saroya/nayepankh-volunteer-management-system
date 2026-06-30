import re


def _handle_empty_input(value, allow_empty):
    if allow_empty and value == "":
        return None

    return value


def get_text(prompt, allow_empty=False):
    while True:
        value = input(prompt).strip()

        value = _handle_empty_input(value, allow_empty)

        if value is None:
            return None

        if value:
            return value

        print("Input cannot be empty.")


def get_positive_integer(prompt, allow_empty=False):
    while True:
        value = input(prompt).strip()

        value = _handle_empty_input(value, allow_empty)

        if value is None:
            return None

        try:
            number = int(value)

            if number > 0:
                return number

            print("Please enter a positive number.")

        except ValueError:
            print("Please enter a valid integer.")


def get_gender(prompt, allow_empty=False):
    valid_genders = ["Male", "Female", "Other"]

    while True:
        gender = input(prompt).strip().title()

        gender = _handle_empty_input(gender, allow_empty)

        if gender is None:
            return None

        if gender in valid_genders:
            return gender

        print("Invalid gender. Choose Male, Female or Other.")


def get_phone(prompt, allow_empty=False):
    while True:
        phone = input(prompt).strip()

        phone = _handle_empty_input(phone, allow_empty)

        if phone is None:
            return None

        if phone.isdigit() and len(phone) == 10:
            return phone

        print("Phone number must contain exactly 10 digits.")


def get_email(prompt, allow_empty=False):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    while True:
        email = input(prompt).strip()

        email = _handle_empty_input(email, allow_empty)

        if email is None:
            return None

        if re.fullmatch(pattern, email):
            return email

        print("Invalid email address.")


def get_availability(prompt, allow_empty=False):
    valid_options = ["Yes", "No"]

    while True:
        availability = input(prompt).strip().title()

        availability = _handle_empty_input(availability, allow_empty)

        if availability is None:
            return None

        if availability in valid_options:
            return availability

        print("Enter either Yes or No.")