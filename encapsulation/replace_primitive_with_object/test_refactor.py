import pytest

from encapsulation.replace_primitive_with_object.after import (
    Priority,
    TaskAfter,
    TaskBoardAfter,
)
from encapsulation.replace_primitive_with_object.before import (
    TaskBefore,
    TaskBoardBefore,
)


def get_tasks_before() -> list[TaskBefore]:
    return [
        TaskBefore(title="Task 1", priority="low"),
        TaskBefore(title="Task 2", priority="critical"),
        TaskBefore(title="Task 3", priority="medium"),
        TaskBefore(title="Task 4", priority="high"),
    ]


def get_tasks_after() -> list[TaskAfter]:
    return [
        TaskAfter(title="Task 1", priority=Priority("low")),
        TaskAfter(title="Task 2", priority=Priority("critical")),
        TaskAfter(title="Task 3", priority=Priority("medium")),
        TaskAfter(title="Task 4", priority=Priority("high")),
    ]


@pytest.mark.parametrize(
    "task_board",
    [TaskBoardBefore(get_tasks_before()), TaskBoardAfter(get_tasks_after())],
)
def test_sort_by_priority(task_board: TaskBoardBefore | TaskBoardAfter):
    if isinstance(task_board, TaskBoardBefore):
        sorted_tasks = task_board.sort_by_priority()
    elif isinstance(task_board, TaskBoardAfter):
        sorted_tasks = task_board.sort_by_priority()

    assert [task.title for task in sorted_tasks] == [
        "Task 2",
        "Task 4",
        "Task 3",
        "Task 1",
    ]


@pytest.mark.parametrize(
    "threshold, expected_titles",
    [
        ("low", ["Task 2", "Task 3", "Task 4"]),
        ("medium", ["Task 2", "Task 4"]),
        ("high", ["Task 2"]),
        ("critical", []),
    ],
)
@pytest.mark.parametrize(
    "task_board",
    [TaskBoardBefore(get_tasks_before()), TaskBoardAfter(get_tasks_after())],
)
def test_get_tasks_greater_than(
    threshold: Priority.Priorities,
    expected_titles: list[str],
    task_board: TaskBoardBefore | TaskBoardAfter,
):
    if isinstance(task_board, TaskBoardBefore):
        result = task_board.get_tasks_greater_than(threshold)
    elif isinstance(task_board, TaskBoardAfter):
        result = task_board.get_tasks_greater_than(Priority(threshold))

    assert [task.title for task in result] == expected_titles
