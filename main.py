from database.database import create_table
from utils.menu import display_menu, get_choice
from services.volunteer_services import VolunteerService


def main():
    create_table()
    service = VolunteerService()

    while True:
        display_menu()
        choice = get_choice()

        match choice:
            case 1:
                service.add_volunteer()
            case 2:
                service.view_all_volunteers()
            case 3:
                service.search_volunteer()
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