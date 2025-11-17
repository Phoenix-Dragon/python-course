
class Car:
    def __init__(self, model:str, brand:str, power:int, fuel_tank:int):
        self.model = model
        self.brand = brand
        self.power = power
        self.fuel_tank = fuel_tank
        self.is_started = False
    
    def start(self):
        if not self.is_started:
            print(f"la {self.brand} a démaré")
            self.is_started = True
        else :
            print(f"la {self.brand} a déjà démaré")

    def stop(self):
        if self.is_started:
            print(f"la {self.brand} est éteinte")
            self.is_started = False
        else : 
            print(f"la {self.brand} a explosé")
    
    def forward(self, kilometers:float):
        if self.fuel_tank > 10 and self.is_started: 
            print(f'La voiture avance de {kilometers} km')
            self.fuel_tank -= 0.05 * kilometers 

kia = Car('Picanto', 'Kia', 69, 32)
kia.start()
print(kia.fuel_tank)
kia.forward(50)
print(kia.fuel_tank)
kia.stop()
