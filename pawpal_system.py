"""PawPal+ system classes.

Skeleton generated from diagrams/uml.mmd. Method bodies are left as stubs
(`pass` / `raise NotImplementedError`) for implementation.
"""

from __future__ import annotations

from enum import Enum
from typing import List, Optional


class Priority(Enum):
    """Task priority levels."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


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
        raise NotImplementedError

    def mark_incomplete(self) -> None:
        raise NotImplementedError

    def update_due_time(self, new_due_time: str) -> None:
        raise NotImplementedError

    def update_priority(self, new_priority: Priority) -> None:
        raise NotImplementedError

    def get_task_summary(self) -> str:
        raise NotImplementedError


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
        raise NotImplementedError

    def remove_task(self, task_description: str) -> None:
        raise NotImplementedError

    def list_tasks(self) -> List[Task]:
        raise NotImplementedError

    def list_incomplete_tasks(self) -> List[Task]:
        raise NotImplementedError

    def find_task(self, task_description: str) -> Optional[Task]:
        raise NotImplementedError

    def get_pet_summary(self) -> str:
        raise NotImplementedError


class Owner:
    """A pet owner with one or more pets."""

    def __init__(self, name: str, email: str) -> None:
        self.name: str = name
        self.email: str = email
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        raise NotImplementedError

    def remove_pet(self, pet_name: str) -> None:
        raise NotImplementedError

    def list_pets(self) -> List[Pet]:
        raise NotImplementedError

    def find_pet(self, pet_name: str) -> Optional[Pet]:
        raise NotImplementedError

    def get_owner_summary(self) -> str:
        raise NotImplementedError


class Scheduler:
    """Builds and organizes a daily care plan for an owner's pets."""

    def __init__(self, owner: Owner) -> None:
        self.owner: Owner = owner
        self.scheduled_tasks: List[Task] = []
        self.skipped_tasks: List[Task] = []

    def get_all_tasks(self) -> List[Task]:
        raise NotImplementedError

    def get_incomplete_tasks(self) -> List[Task]:
        raise NotImplementedError

    def sort_tasks_by_priority(self) -> List[Task]:
        raise NotImplementedError

    def sort_tasks_by_due_time(self) -> List[Task]:
        raise NotImplementedError

    def generate_daily_plan(self) -> List[Task]:
        raise NotImplementedError

    def mark_task_complete(self, pet_name: str, task_description: str) -> None:
        raise NotImplementedError

    def get_schedule_summary(self) -> str:
        raise NotImplementedError
