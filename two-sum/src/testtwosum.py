import pytest
from twosum import findPair

class TestTwoSum:
    def test_it_returns_empty_for_empty_list(self):
        assert(findPair([], 1) == [])
