import pytest

from odin.source.core.update_version import version_verification

parameters = [
    ([0, 0, 1], [0, 0, 2], False, True),  # 0
    ([0, 0, 1], [0, 1, 0], False, True),  # 1
    ([0, 0, 1], [1, 0, 0], False, True),  # 2
    ([0, 1, 0], [1, 0, 0], False, True),  # 3
    ([0, 0, 2], [0, 0, 2], False, False),  # 4
    ([0, 0, 2], [0, 0, 1], False, False),  # 5
    ([0, 0, 1], [0, 0, 2, 1], True, True),  # 6
    ([0, 0, 1], [0, 0, 2, 1], False, False),  # 7
    ([0, 0, 2], [0, 0, 1, 2], True, False),  # 8
    ([0, 0, 1, 1], [0, 0, 2], False, True),  # 9
    ([0, 0, 1, 1], [0, 0, 2], True, True),  # 10
    ([0, 0, 1, 1], [0, 0, 1], False, True),  # 11
    ([0, 0, 1, 1], [0, 0, 1, 2], True, True),  # 12
    ([0, 0, 1, 1], [0, 0, 1, 2], False, False),  # 13
]


@pytest.mark.parametrize("actual, new, beta, expected", parameters)
def test_version_verification(actual, new, beta, expected):
    assert version_verification(actual, new, beta) == expected
