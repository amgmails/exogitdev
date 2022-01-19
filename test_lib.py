from lib import average
def test_average():
    input1 = [10,15,5,35,25,30]
    expected_result = 20
    
    actual_result = average(input1)
    assert expected_result == actual_result

test_average()