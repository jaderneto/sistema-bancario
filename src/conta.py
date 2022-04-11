from datetime import datetime


class Conta:
    def __init__(self, owner):
        self.value = 0
        self.moviments = []
        self.creation_at = datetime.now()
        self.owner = owner

    def deposit(self, amount):
        self.value += amount
        self.moviments.append(('deposit', datetime.now(), amount))

    def withdraw(self, amount):
        self.value -= amount
        self.moviments.append(('withdraw', datetime.now(), amount))

    def getinfo(self):
        print('Conta corrente do %s possui um saldo de R$ %.2f' % (self.owner.name, self.value))

    def show_moviments(self):
        print('----------------------------- Extrato bancario ---------------------------------')
        for i in range(len(self.moviments)):
            print('Tipo: %s | Valor movimentado: R$ %.2f | Data: %s' % (self.moviments[i][0], self.moviments[i][2], self.moviments[i][1]))

        print('--------------------------------------------------------------------------------')
