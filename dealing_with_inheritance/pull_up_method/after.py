class PetAfter:
    def __init__(self, name: str) -> None:
        self.name = name

    def identity_label(self) -> str:
        return f"{self.name} is a pet"

class CatAfter(PetAfter):

    def sound(self) -> str:
        return "meow"


class DogAfter(PetAfter):

    def sound(self) -> str:
        return "woof"
