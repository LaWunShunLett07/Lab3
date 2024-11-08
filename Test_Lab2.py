import Lab2
import Lab2.lab2

def test_average_temperature():
    test_list = [24.0, 13.0, 2.0, 1.0]
    expected_list = sum(test_list)/len(test_list)
    average_list = Lab2.lab2.calc_average_temperature(test_list)
    assert average_list == expected_list

def test_calc_median_temperature():
    test_list = [1.0, 2.0, 13.0, 24.0]
    expected_median = (2.0 + 13.0) / 2  # Median for even list
    median = Lab2.lab2.calc_median_temperature(test_list)
    assert median == expected_median

def test_calc_min_max_temperature():
    test_list = [1.0, 2.0, 13.0, 24.0]
    expected_min = 1
    expected_max = 24
    inMin, inMax = Lab2.lab2.calc_min_max_temperature(test_list, test_list)
    assert inMin == expected_min
    assert inMax == expected_max