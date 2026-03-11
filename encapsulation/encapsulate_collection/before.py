class ReadingGroupBefore:
    def __init__(self, name: str, members: list[str] | None = None):
        self.name = name
        self.members = members or []


class Client1ExampleBefore:
    def __init__(self, group: ReadingGroupBefore):
        self.group = group

    def enroll_trial_members(self, members: list[str]):
        self.group.members.extend(members)


class Client2ExampleBefore:
    def __init__(self, group: ReadingGroupBefore):
        self.group = group

    def remove_inactive_members(self, inactive_members: list[str]):
        for member in inactive_members:
            if member in self.group.members:
                self.group.members.remove(member)


class Client3ExampleBefore:
    def __init__(self, group: ReadingGroupBefore):
        self.group = group

    def replace_all_members(self, new_members: list[str]):
        self.group.members = new_members
