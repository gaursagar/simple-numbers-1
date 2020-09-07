from Numbers import Numbers

def test_is_even():
    instance = Numbers()
    assert instance.is_even(5) == False, "should be False"
    assert instance.is_even(4) == True, "should be True"
    assert instance.is_even(0) == True, "should be True"
    assert instance.is_even(-2) == True, "should be True"
    assert instance.is_even(-5) == False, "should be False"

def test_add():
    instance = Numbers()
    assert instance.add(1) == 1, "should be 1"
    assert instance.add(1, 2) == 1+2, "should be 3"
    assert instance.add(1, 2, -3) == 1+2-3, "should be 0"
    assert instance.add(1, 2, 1.05) == 1+2+1.05, "should be 4.05"
