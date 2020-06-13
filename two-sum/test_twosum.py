import pytest
from twosum import two_sum

class TestTwoSum:
    def test_it_returns_empty_for_empty_list(self):
        assert(two_sum(nums=[], target=1) == [])
    
    def test_one_plus_one_is_two(self):
        assert(two_sum(nums=[1, 1], target=1) == [0, 1])
