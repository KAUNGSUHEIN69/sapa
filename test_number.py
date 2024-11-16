import number
def test_calculate_sum_of_even_numbers():
    
    test_arr = [12,20,22,3,4,5,6,9]
    result = number.calculate_sum_of_even_numbers(test_arr)
    expect = 64
    assert result == expect

def test_get_first_n_smallest_numbers():
    test_arr = [12,20,22,3,4,5,6,9]
    result = number.get_first_n_smallest_numbers(test_arr,4)
    expect = [3,4,5,6]
    assert result == expect

def test_find_largest_number():
    test_arr = [12,20,22,3,4,5,6,9]
    result = number.find_largest_number(test_arr)
    expect = 22
    assert result == expect
