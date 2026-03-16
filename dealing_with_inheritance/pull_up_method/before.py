class PetBefore:
    def __init__(self, name: str) -> None:
        self.name = name


class CatBefore(PetBefore):
    def identity_label(self) -> str:
        return f"{self.name} is a pet"

    def sound(self) -> str:
        return "meow"


class DogBefore(PetBefore):
    def identity_label(self) -> str:
        return f"{self.name} is a pet"

    def sound(self) -> str:
        return "woof"
