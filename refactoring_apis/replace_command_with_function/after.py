class GreetingServiceAfter:
    def build_greeting(self, name: str, is_formal: bool) -> str:
        if is_formal:
            return f"Hello, {name}. Welcome back."
        return f"Hi {name}!"
