from typing import Literal


class Priority:
    Priorities = Literal["low", "medium", "high", "critical"]
    _order = {"low": 1, "medium": 2, "high": 3, "critical": 4}

    def __init__(self, value: Priorities):
        self.value = value

    def rank(self) -> int:
        return self._order[self.value]

    def is_greater_than(self, other: Priority) -> bool:
        return self.rank() > other.rank()


class TaskAfter:
    def __init__(self, title: str, priority: Priority):
        self.title = title
        self.priority = priority


class TaskBoardAfter:
    def __init__(self, tasks: list[TaskAfter]) -> None:
        self.tasks = tasks

    def sort_by_priority(self) -> list[TaskAfter]:
        return sorted(self.tasks, key=lambda task: task.priority.rank(), reverse=True)

    def get_tasks_greater_than(self, priority: Priority) -> list[TaskAfter]:
        return [task for task in self.tasks if task.priority.is_greater_than(priority)]
