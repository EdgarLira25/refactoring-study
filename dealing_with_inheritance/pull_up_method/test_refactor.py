import pytest

from dealing_with_inheritance.pull_up_method.after import CatAfter, DogAfter
from dealing_with_inheritance.pull_up_method.before import CatBefore, DogBefore


@pytest.mark.parametrize("cat_factory", [CatBefore, CatAfter])
def test_cats(cat_factory):
    pet = cat_factory(name="Luna")
    assert pet.identity_label() == f"Luna is a pet"
    assert pet.sound() == "meow"


@pytest.mark.parametrize("dog_factory", [DogBefore, DogAfter])
def test_dogs(dog_factory):
    pet = dog_factory(name="Bolt")
    assert pet.identity_label() == f"Bolt is a pet"
    assert pet.sound() == "woof"
