import pytest

from dealing_with_inheritance.pull_up_field.after import DesignerAfter, EngineerAfter
from dealing_with_inheritance.pull_up_field.before import DesignerBefore, EngineerBefore


@pytest.mark.parametrize("engineer_factory", [EngineerBefore, EngineerAfter])
def test_engineers(engineer_factory):
    engineer = engineer_factory(name="Ana")
    assert engineer.base_salary == 6000.0
    assert engineer.monthly_total() == 7200.0


@pytest.mark.parametrize("designer_factory", [DesignerBefore, DesignerAfter])
def test_designers(designer_factory):
    designer = designer_factory(name="Bia")
    assert designer.base_salary == 6000.0
    assert designer.monthly_total() == 6900.0
