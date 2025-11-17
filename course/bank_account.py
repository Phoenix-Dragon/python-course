# Créer une classe BankAccount.
# Le constructeur initialisera deux attributs, name et balance avec les
# valeurs par défaut respectives 'John' et 1000.
# Ensuite, implémenter les méthodes suivantes :
# - deposit : déposer une somme
# - withdraw : retirer une somme
# - display : afficher le nom du titulaire ainsi que le solde
# Enfin, instancier au moins deux comptes différents et réaliser des
# opérations dessus.

class BankAccount :

    def __init__(self, name:str = 'John', balance:float = 1000):
        self.name = name
        self.balance = balance
    
    def deposit(self, depos:float):
        if depos > 0 :
            self.balance += depos

    def withdraw(self, retrait:float):
        if retrait > 0:
            self.balance -= retrait

    def display(self):
        print(f' Bonjour {self.name}, vous avez {self.balance}€ sur votre compte !')

thomas = BankAccount('Thomas', 1300)
print(thomas.balance)
thomas.withdraw(500)
print(thomas.balance)
thomas.deposit(300)
thomas.display()
