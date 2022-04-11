from src.conta import *
from src.person import *
from datetime import datetime

p1 = Person('Jader', '05825399356', 'Male')
c1 = Conta(datetime.now(), p1)
c1.deposit(100)
c1.deposit(300)

print(c1.value)
print(c1.owner.cpf)