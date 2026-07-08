"""PawPal+ demo entry point.

Builds a sample owner with two pets and several care tasks, then prints
today's generated schedule to the terminal.
"""

from pawpal_system import Owner, Pet, Task, Priority, Scheduler

TODAY = "2026-07-07"


def build_sample_owner() -> Owner:
    """Create an owner with two pets and a handful of care tasks."""
    owner = Owner("Jordan", "jordan@example.com")

    mochi = Pet("Mochi", "dog", "Shiba Inu", 3)
    mochi.add_task(
        Task(
            "Morning walk",
            due_time="08:00",
            due_date=TODAY,
            priority=Priority.HIGH,
            duration_minutes=30,
            rationale="Dogs need morning exercise to burn energy.",
        )
    )
    mochi.add_task(
        Task(
            "Breakfast",
            due_time="09:00",
            due_date=TODAY,
            priority=Priority.HIGH,
            duration_minutes=10,
            rationale="Consistent feeding time keeps digestion regular.",
        )
    )
    mochi.add_task(
        Task(
            "Evening enrichment",
            due_time="17:30",
            due_date=TODAY,
            priority=Priority.MEDIUM,
            duration_minutes=20,
            rationale="Mental stimulation prevents boredom.",
        )
    )

    whiskers = Pet("Whiskers", "cat", "Tabby", 5)
    whiskers.add_task(
        Task(
            "Litter box cleaning",
            due_time="10:00",
            due_date=TODAY,
            priority=Priority.HIGH,
            duration_minutes=5,
            rationale="Cats refuse a dirty litter box.",
        )
    )
    whiskers.add_task(
        Task(
            "Dinner",
            due_time="18:00",
            due_date=TODAY,
            priority=Priority.MEDIUM,
            duration_minutes=10,
            rationale="Evening meal for a healthy routine.",
        )
    )

    owner.add_pet(mochi)
    owner.add_pet(whiskers)
    return owner


def main() -> None:
    owner = build_sample_owner()

    scheduler = Scheduler(owner)
    scheduler.generate_daily_plan()

    print("=" * 48)
    print(f"Today's Schedule — {TODAY}")
    print("=" * 48)
    print(scheduler.get_schedule_summary())


if __name__ == "__main__":
    main()
