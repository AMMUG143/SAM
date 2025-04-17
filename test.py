
from add_numbers import add_numbers
def test_add_numbers():
    # Test case 1: Positive numbers
    assert add_numbers(5, 3) == 8, "Test case 1 failed"
    
    # Test case 2: Negative numbers
    assert add_numbers(-5, -3) == -8, "Test case 2 failed"
    
    # Test case 3: Zero
    assert add_numbers(0, 0) == 0, "Test case 3 failed"
    
    # Test case 4: Mixed numbers
    assert add_numbers(-5, 5) == 0, "Test case 4 failed"
    
    print("All test cases passed!")