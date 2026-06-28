def display_menu():
    print("\n" + "=" * 50)
    print("    NayePankh Volunteer Management System")
    print("=" * 50)
    print("1. Add Volunteer")
    print("2. View All Volunteers")
    print("3. Search Volunteer")
    print("4. Filter Volunteers")
    print("5. Update Volunteer")
    print("6. Delete Volunteer")
    print("7. Generate Report")
    print("8. Export to CSV")
    print("9. Exit")
    print("=" * 50)


def get_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-9): "))

            if 1 <= choice <= 9:
                return choice

            print("Invalid choice! Please enter a number between 1 and 9.")

        except ValueError:
            print("Please enter a valid number.")