from src.conta import *
from src.person import *
from datetime import datetime

p1 = Person('Jader', '05825399356', 'Male')
c1 = Conta(datetime.now(), p1)
c1.deposit(100)
c1.deposit(300)

p2 = Person('Taiane', '54399235534', 'Female')
c2 = Conta(datetime.now(), p2)
c2.deposit(500)

print(c1.owner.name + ': ', c1.value)
print(c2.owner.name + ': ', c2.value)