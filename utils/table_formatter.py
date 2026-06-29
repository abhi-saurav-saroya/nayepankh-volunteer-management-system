from models.volunteers import Volunteer


def print_volunteers(volunteers: list[Volunteer]):

    if not volunteers:
        print("\nNo volunteers found.")
        return

    print("\n" + "=" * 150)

    print(
        f"{'ID':<5}"
        f"{'Name':<20}"
        f"{'Age':<6}"
        f"{'Gender':<10}"
        f"{'Phone':<15}"
        f"{'Email':<30}"
        f"{'City':<15}"
        f"{'Skill':<20}"
        f"{'Available':<12}"
        f"{'Join Date':<15}"
    )

    print("-" * 150)

    for volunteer in volunteers:
        print(
            f"{volunteer.id:<5}"
            f"{volunteer.name:<20}"
            f"{volunteer.age:<6}"
            f"{volunteer.gender:<10}"
            f"{volunteer.phone:<15}"
            f"{volunteer.email:<30}"
            f"{volunteer.city:<15}"
            f"{volunteer.skill:<20}"
            f"{volunteer.availability:<12}"
            f"{volunteer.join_date:<15}"
        )

    print("=" * 150)