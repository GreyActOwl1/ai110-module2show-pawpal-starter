"""Tests for core PawPal+ behaviors."""

from pawpal_system import Owner, Pet, Task, Priority, Scheduler


def make_task(description: str = "Morning walk") -> Task:
    return Task(
        description=description,
        due_time="08:00",
        due_date="2026-07-08",
        priority=Priority.HIGH,
        duration_minutes=30,
    )


def test_adding_task_to_pet():
    pet = Pet("Mochi", "dog", "Shiba Inu", 3)
    assert pet.list_tasks() == []

    task = make_task()
    pet.add_task(task)

    tasks = pet.list_tasks()
    assert len(tasks) == 1
    assert tasks[0] is task
    assert pet.find_task("Morning walk") is task


def test_mark_task_complete_changes_status():
    task = make_task()
    assert task.is_complete is False

    task.mark_complete()
    assert task.is_complete is True

    task.mark_incomplete()
    assert task.is_complete is False


def test_scheduler_mark_task_complete_changes_status():
    owner = Owner("Jordan", "jordan@example.com")
    pet = Pet("Mochi", "dog", "Shiba Inu", 3)
    task = make_task()
    pet.add_task(task)
    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    assert task.is_complete is False

    scheduler.mark_task_complete("Mochi", "Morning walk")

    assert task.is_complete is True
    assert task not in pet.list_incomplete_tasks()
