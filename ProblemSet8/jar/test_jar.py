from jar import Jar

def test_init():
    jar = Jar()
    jar.__init__(9)
    assert jar.capacity == 9
def test_deposit():
    jar = Jar()
    jar.deposit(9)
    assert jar.__str__() == "🍪🍪🍪🍪🍪🍪🍪🍪🍪"
def test_withdraw():
    jar = Jar()
    jar.deposit(9)
    jar.withdraw(8)
    assert jar.__str__() == "🍪"
def test_fill():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw (10)
    jar.deposit(9)
    jar.withdraw(8)
    assert jar.__str__() == "🍪"
