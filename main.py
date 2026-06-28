from database.database import create_table
from utils.menu import display_menu, get_choice


def main():
    create_table()

    while True:
        display_menu()
        choice = get_choice()

        match choice:
            case 1:
                print("\n[Add Volunteer - Coming Soon]")
            case 2:
                print("\n[View Volunteers - Coming Soon]")
            case 3:
                print("\n[Search Volunteer - Coming Soon]")
            case 4:
                print("\n[Filter Volunteers - Coming Soon]")
            case 5:
                print("\n[Update Volunteer - Coming Soon]")
            case 6:
                print("\n[Delete Volunteer - Coming Soon]")
            case 7:
                print("\n[Generate Report - Coming Soon]")
            case 8:
                print("\n[Export to CSV - Coming Soon]")
            case 9:
                print("\nThank you for using NayePankh Volunteer Management System!")
                break


if __name__ == "__main__":
    main()