from database.database import (
    get_total_volunteers,
    get_available_volunteers_count,
    get_unavailable_volunteers_count,
    get_volunteers_by_city,
    get_volunteers_by_skill
)


class ReportService:

    def generate_report(self):
        total = get_total_volunteers()
        available = get_available_volunteers_count()
        unavailable = get_unavailable_volunteers_count()
        city_report = get_volunteers_by_city()
        skill_report = get_volunteers_by_skill()

        print("\n" + "=" * 50)
        print("         Volunteer Report")
        print("=" * 50)

        print(f"Total Volunteers      : {total}")
        print(f"Available Volunteers  : {available}")
        print(f"Unavailable Volunteers: {unavailable}")

        print("\nVolunteers by City")
        print("-" * 50)
        for city, count in city_report:
            print(f"{city:<25}{count}")

        print("\nVolunteers by Skill")
        print("-" * 50)
        for skill, count in skill_report:
            print(f"{skill:<25}{count}")

        print("=" * 50)