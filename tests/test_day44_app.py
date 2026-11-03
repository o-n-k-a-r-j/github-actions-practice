
from day44_app import calculate_total

def test_multiple_items():
    assert calculate_total([100, 200, 50]) == 350

def test_empty_cart():
    assert calculate_total([]) == 0

