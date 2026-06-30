from database.database import create_table
from utils.menu import display_menu, get_choice
from services.volunteer_services import VolunteerService
from services.report_service import ReportService
from services.export_service import ExportService


def main():
    create_table()
    service = VolunteerService()
    report_service = ReportService()
    export_service = ExportService()

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
                service.filter_volunteers()
            case 5:
                service.update_volunteer()
            case 6:
                service.delete_volunteer()
            case 7:
                report_service.generate_report()
            case 8:
                export_service.export_to_csv()
            case 9:
                print("\nThank you for using NayePankh Volunteer Management System!")
                break


if __name__ == "__main__":
    main()