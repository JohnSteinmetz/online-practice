import pytest
from twosum import two_sum

class TestTwoSum:
    def test_it_returns_empty_for_empty_list(self):
        assert(two_sum(nums=[], target=1) == [])
    
    def test_one_plus_one_is_two(self):
        assert(two_sum(nums=[1, 1], target=2) == [0, 1])

    def test_returns_empty_for_one_number_list(self):
        assert(two_sum(nums=[1], target=1) == [])

    def test_for_unique_positive_numbers(self):
        assert(two_sum(nums=[1, 2, 3, 4, 5], target=9) == [3, 4])
    
    def test_negative_numbers(self):
        assert(two_sum(nums=[-1, 2, 4], target=1) == [0, 1])
        assert(two_sum(nums=[-2, 3, -4], target=-6) == [0, 2])