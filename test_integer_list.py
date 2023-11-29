import pytest
from integer_list import IntegerList

# Test add_integer method
@pytest.mark.parametrize("nums, expected_result", [([1, 2, 3], [1, 2, 3]),
                                                   ([5, 10, 15], [5, 10, 15]),
                                                   ([], [])])
def test_add_integer(nums, expected_result):
    integer_list = IntegerList()
    for num in nums:
        integer_list.add_integer(num)
    assert integer_list.integers == expected_result


# Test remove_integer method
@pytest.mark.parametrize("initial_nums, num_to_remove, expected_result", [([1, 2, 3], 2, [1, 3]),
                                                                         ([5, 10, 15], 10, [5, 15]),
                                                                         ([], 5, [])])
def test_remove_integer(initial_nums, num_to_remove, expected_result):
    integer_list = IntegerList()
    integer_list.integers = initial_nums
    integer_list.remove_integer(num_to_remove)
    assert integer_list.integers == expected_result


# Test get_average method
@pytest.mark.parametrize("nums, expected_result", [([1, 2, 3], 2.0),
                                                   ([5, 10, 15], 10.0),
                                                   ([], None)])
def test_get_average(nums, expected_result):
    integer_list = IntegerList()
    integer_list.integers = nums
    assert integer_list.get_average() == expected_result


# Test get_max method
@pytest.mark.parametrize("nums, expected_result", [([1, 2, 3], 3),
                                                   ([5, 10, 15], 15),
                                                   ([], None)])
def test_get_max(nums, expected_result):
    integer_list = IntegerList()
    integer_list.integers = nums
    assert integer_list.get_max() == expected_result


# Test get_min method
@pytest.mark.parametrize("nums, expected_result", [([1, 2, 3], 1),
                                                   ([5, 10, 15], 5),
                                                   ([], None)])
def test_get_min(nums, expected_result):
    integer_list = IntegerList()
    integer_list.integers = nums
    assert integer_list.get_min() == expected_result
