from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("hello, world") == 0

def test_hi():
    assert value("Hi") == 20
    assert value("hi there") == 20

def test_other():
    assert value("What's up") == 100
    assert value("Good morning") == 100