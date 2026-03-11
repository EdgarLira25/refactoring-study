class ReadingGroupAfter:
    def __init__(self, name: str, members: list[str]):
        self.name = name
        self.members = members or []

    def remove(self, members_to_remove: list[str]):
        for member in members_to_remove:
            if member in self.members:
                self.members.remove(member)

    def replace_members(self, members: list[str]):
        self.members = members

    def add_members(self, members: list[str]):
        self.members.extend(members)


class Client1ExampleAfter:
    def __init__(self, group: ReadingGroupAfter):
        self.group = group

    def enroll_trial_members(self, members: list[str]):
        self.group.add_members(members)


class Client2ExampleAfter:
    def __init__(self, group: ReadingGroupAfter):
        self.group = group

    def remove_inactive_members(self, inactive_members: list[str]):
        self.group.remove(inactive_members)


class Client3ExampleAfter:
    def __init__(self, group: ReadingGroupAfter):
        self.group = group

    def replace_all_members(self, new_members: list[str]):
        self.group.replace_members(new_members)
