from src.conta import *
from src.person import *

p1 = Person('Jader', '05825399356', 'Male')
c1 = Conta(p1)
c1.deposit(100)
c1.deposit(300)

p2 = Person('Taiane', '54399235534', 'Female')
c2 = Conta(p2)
c2.deposit(500)

c1.getinfo()
c1.show_moviments()
