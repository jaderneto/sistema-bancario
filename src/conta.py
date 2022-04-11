from datetime import datetime


class Conta:
    def __init__(self, creating_at, owner):
        self.value = 0
        self.moviments = []
        self.creating_at = creating_at
        self.owner = owner

    def deposit(self, amount):
        self.value += amount
        self.moviments.append(('deposit', datetime.now(), amount))

    def withdraw(self, amount):
        self.value -= amount
        self.moviments.append(('withdraw', datetime.now(), amount))