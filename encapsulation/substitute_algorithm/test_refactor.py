import pytest

from encapsulation.substitute_algorithm.after import TagAnalyticsAfter
from encapsulation.substitute_algorithm.before import TagAnalyticsBefore


def tag_analytics():
    return [TagAnalyticsBefore(), TagAnalyticsAfter()]

@pytest.mark.parametrize("analytics", tag_analytics())
@pytest.mark.parametrize(
    "tags, expected",
    [
        ([" Python ", "python", "Data", "", "data", "ai"], ["python", "data", "ai"]),
        (["python", "ai", "python", "data", "ai", "ai"], ['python', 'ai', 'data']),
        (["zeta", "alpha", "alpha", "zeta"], ['zeta', 'alpha']),
        (["   ", ""], []),
        ([], []),
    ],
)
def test_normalize_tags(analytics: TagAnalyticsBefore, tags: list[str], expected: list[str]):
    assert analytics.normalize_tags(tags) == expected

@pytest.mark.parametrize("analytics", tag_analytics())
@pytest.mark.parametrize(
    "tags, expected_top",
    [
        (["python", "ai", "python", "data", "ai", "ai"], "ai"),
        (["zeta", "alpha", "alpha", "zeta"], "alpha"),
        (["   ", ""], None),
    ],
)
def test_top_tag(analytics: TagAnalyticsBefore, tags: list[str], expected_top: str | None):
    assert analytics.top_tag(tags) == expected_top

@pytest.mark.parametrize("analytics", tag_analytics())
@pytest.mark.parametrize(
    "tags, expected_summary",
    [
        (["python", "ai", "python", "data", "ai", "ai"], "Tags: 3 | Top: ai"),
        (["  ", ""], "Tags: 0 | Top: none"),
    ],
)
def test_summary(analytics: TagAnalyticsBefore | TagAnalyticsAfter, tags: list[str], expected_summary: str):
    assert analytics.summary(tags) == expected_summary
