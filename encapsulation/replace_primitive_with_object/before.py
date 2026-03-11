class TaskBefore:
    def __init__(self, title: str, priority: str):
        self.title = title
        self.priority = priority


class TaskBoardBefore:
    def __init__(self, tasks: list[TaskBefore]) -> None:
        self.tasks = tasks

    def get_tasks_greater_than(self, priority: str) -> list[TaskBefore]:

        result = []

        if priority == "low":
            for task in self.tasks:
                if task.priority == "medium":
                    result.append(task)
                elif task.priority == "high":
                    result.append(task)
                elif task.priority == "critical":
                    result.append(task)

        elif priority == "medium":
            for task in self.tasks:
                if task.priority == "high":
                    result.append(task)
                elif task.priority == "critical":
                    result.append(task)

        elif priority == "high":
            for task in self.tasks:
                if task.priority == "critical":
                    result.append(task)

        elif priority == "critical":
            return []

        return result

    def sort_by_priority(self) -> list[TaskBefore]:
        order = {"low": 1, "medium": 2, "high": 3, "critical": 4}
        return sorted(
            self.tasks, key=lambda task: order.get(task.priority, 0), reverse=True
        )
