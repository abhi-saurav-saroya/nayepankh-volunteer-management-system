import csv

from database.database import get_all_volunteers


class ExportService:

    def export_to_csv(self):
        volunteers = get_all_volunteers()

        if not volunteers:
            print("\nNo volunteers available to export.")
            return

        filename = input("\nEnter CSV filename (without extension): ").strip()
        if not filename:
            filename = "volunteers"

        filename = "exports/" + filename + ".csv"

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "ID",
                "Name",
                "Age",
                "Gender",
                "Phone",
                "Email",
                "City",
                "Skill",
                "Availability",
                "Join Date"
            ])

            for volunteer in volunteers:
                writer.writerow([
                    volunteer.id,
                    volunteer.name,
                    volunteer.age,
                    volunteer.gender,
                    volunteer.phone,
                    volunteer.email,
                    volunteer.city,
                    volunteer.skill,
                    volunteer.availability,
                    volunteer.join_date
                ])

        print(f"\nData exported successfully to '{filename}'.")