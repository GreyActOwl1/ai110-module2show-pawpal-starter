"""PawPal+ system classes.

Generated from diagrams/uml.mmd. Implements the core domain model:
Owner -> Pet -> Task, plus a Scheduler that builds a daily care plan.
"""

from __future__ import annotations

from enum import Enum
from typing import List, Optional


class Priority(Enum):
    """Task priority levels."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    @property
    def rank(self) -> int:
        """Higher number = more urgent. Used for sorting."""
        return {Priority.LOW: 1, Priority.MEDIUM: 2, Priority.HIGH: 3}[self]


class Task:
    """A single pet care task."""

    def __init__(
        self,
        description: str,
        due_time: str,
        due_date: str,
        priority: Priority,
        duration_minutes: int,
        is_complete: bool = False,
        rationale: str = "",
    ) -> None:
        self.description: str = description
        self.due_time: str = due_time
        self.due_date: str = due_date
        self.priority: Priority = priority
        self.duration_minutes: int = duration_minutes
        self.is_complete: bool = is_complete
        self.rationale: str = rationale

    def mark_complete(self) -> None:
        """Mark this task as done."""
        self.is_complete = True

    def mark_incomplete(self) -> None:
        """Mark this task as not yet done."""
        self.is_complete = False

    def update_due_time(self, new_due_time: str) -> None:
        """Change the task's due time."""
        self.due_time = new_due_time

    def update_priority(self, new_priority: Priority) -> None:
        """Change the task's priority level."""
        self.priority = new_priority

    def get_task_summary(self) -> str:
        """Return a one-line human-readable summary of this task."""
        status = "✓" if self.is_complete else "○"
        summary = (
            f"{status} {self.due_time} — {self.description} "
            f"({self.duration_minutes} min) [priority: {self.priority.value}]"
        )
        if self.rationale:
            summary += f"\n    why: {self.rationale}"
        return summary


class Pet:
    """A pet owned by an Owner, with a list of care tasks."""

    def __init__(
        self,
        name: str,
        species: str,
        breed: str,
        age: int,
    ) -> None:
        self.name: str = name
        self.species: str = species
        self.breed: str = breed
        self.age: int = age
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Add a care task to this pet."""
        self.tasks.append(task)

    def remove_task(self, task_description: str) -> None:
        """Remove all tasks matching the given description."""
        self.tasks = [
            task for task in self.tasks if task.description != task_description
        ]

    def list_tasks(self) -> List[Task]:
        """Return a copy of all of this pet's tasks."""
        return list(self.tasks)

    def list_incomplete_tasks(self) -> List[Task]:
        """Return this pet's tasks that are not yet complete."""
        return [task for task in self.tasks if not task.is_complete]

    def find_task(self, task_description: str) -> Optional[Task]:
        """Return the first task matching the description, or None."""
        for task in self.tasks:
            if task.description == task_description:
                return task
        return None

    def get_pet_summary(self) -> str:
        """Return a multi-line summary of this pet and its tasks."""
        incomplete = len(self.list_incomplete_tasks())
        header = (
            f"{self.name} ({self.breed} {self.species}, age {self.age}) — "
            f"{len(self.tasks)} task(s), {incomplete} incomplete"
        )
        if not self.tasks:
            return header
        lines = [header]
        for task in self.tasks:
            lines.append("  " + task.get_task_summary())
        return "\n".join(lines)


class Owner:
    """A pet owner with one or more pets."""

    def __init__(self, name: str, email: str) -> None:
        self.name: str = name
        self.email: str = email
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner."""
        self.pets.append(pet)

    def remove_pet(self, pet_name: str) -> None:
        """Remove all pets matching the given name."""
        self.pets = [pet for pet in self.pets if pet.name != pet_name]

    def list_pets(self) -> List[Pet]:
        """Return a copy of this owner's list of pets."""
        return list(self.pets)

    def find_pet(self, pet_name: str) -> Optional[Pet]:
        """Return the first pet matching the name, or None."""
        for pet in self.pets:
            if pet.name == pet_name:
                return pet
        return None

    def get_owner_summary(self) -> str:
        """Return a one-line summary of this owner and their pets."""
        header = f"{self.name} <{self.email}> — {len(self.pets)} pet(s)"
        if not self.pets:
            return header
        pet_names = ", ".join(pet.name for pet in self.pets)
        return f"{header}: {pet_names}"


class Scheduler:
    """Builds and organizes a daily care plan for an owner's pets."""

    def __init__(self, owner: Owner) -> None:
        self.owner: Owner = owner
        self.scheduled_tasks: List[Task] = []
        self.skipped_tasks: List[Task] = []

    def get_all_tasks(self) -> List[Task]:
        """Return every task across all of the owner's pets."""
        tasks: List[Task] = []
        for pet in self.owner.list_pets():
            tasks.extend(pet.list_tasks())
        return tasks

    def get_incomplete_tasks(self) -> List[Task]:
        """Return every incomplete task across all of the owner's pets."""
        return [task for task in self.get_all_tasks() if not task.is_complete]

    def sort_tasks_by_priority(self) -> List[Task]:
        """Return all tasks sorted by priority, then by due time."""
        # Most urgent first; ties broken by earlier due time for a stable plan.
        return sorted(
            self.get_all_tasks(),
            key=lambda task: (-task.priority.rank, task.due_time),
        )

    def sort_tasks_by_due_time(self) -> List[Task]:
        """Return all tasks sorted by due time, earliest first."""
        return sorted(self.get_all_tasks(), key=lambda task: task.due_time)

    def generate_daily_plan(self, available_minutes: Optional[int] = None) -> List[Task]:
        """Build an ordered plan of incomplete tasks.

        Tasks are considered in priority order (ties broken by due time). When
        ``available_minutes`` is given, tasks that no longer fit in the
        remaining time budget are moved to ``skipped_tasks`` instead of being
        scheduled. Completed tasks are never scheduled.
        """
        self.scheduled_tasks = []
        self.skipped_tasks = []

        candidates = [
            task
            for task in self.sort_tasks_by_priority()
            if not task.is_complete
        ]

        remaining = available_minutes
        for task in candidates:
            if remaining is not None and task.duration_minutes > remaining:
                self.skipped_tasks.append(task)
                continue
            self.scheduled_tasks.append(task)
            if remaining is not None:
                remaining -= task.duration_minutes

        # Present the finalized plan in the order it will happen during the day.
        self.scheduled_tasks.sort(key=lambda task: task.due_time)
        return list(self.scheduled_tasks)

    def mark_task_complete(self, pet_name: str, task_description: str) -> None:
        """Mark a named pet's task complete, raising if either is missing."""
        pet = self.owner.find_pet(pet_name)
        if pet is None:
            raise ValueError(f"No pet named {pet_name!r}")
        task = pet.find_task(task_description)
        if task is None:
            raise ValueError(
                f"No task {task_description!r} for pet {pet_name!r}"
            )
        task.mark_complete()

    def get_schedule_summary(self) -> str:
        """Return a multi-line summary of the scheduled and skipped tasks."""
        lines = [f"Daily plan for {self.owner.name}:"]
        if self.scheduled_tasks:
            for task in self.scheduled_tasks:
                lines.append("  " + task.get_task_summary())
        else:
            lines.append("  (no tasks scheduled)")

        if self.skipped_tasks:
            lines.append("Skipped (out of time):")
            for task in self.skipped_tasks:
                lines.append("  " + task.get_task_summary())

        return "\n".join(lines)
