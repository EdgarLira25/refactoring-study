class GreetingCommandBefore:
    def __init__(self, name: str, is_formal: bool) -> None:
        self.name = name
        self.is_formal = is_formal

    def execute(self) -> str:
        if self.is_formal:
            return f"Hello, {self.name}. Welcome back."
        return f"Hi {self.name}!"


class GreetingServiceBefore:
    def build_greeting(self, name: str, is_formal: bool) -> str:
        command = GreetingCommandBefore(name=name, is_formal=is_formal)
        return command.execute()
