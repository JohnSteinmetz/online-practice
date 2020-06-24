from src.search_insert_position import Solution
import pytest

class TestSearchPosition:
    def test_return_0_with_empty_list(self):
        assert(Solution.searchInsert(self, nums = [], target = 1) == 0)

    def test_return_index_of_target_largest_value(self):
        assert(Solution.searchInsert(self, nums = [1,2,3,4], target = 5) == 4)

    def test_value_in_list(self):
        assert(Solution.searchInsert(self, nums = [1, 3, 5, 6], target = 3) == 1)

    def test_value_not_in_list(self):
        assert(Solution.searchInsert(self, nums = [1, 2, 5, 6], target = 3) == 2)