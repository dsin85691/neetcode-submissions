class SuperHero:
    """
    A class to represent a superhero.
    
    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """
    
    def __init__(self, name: str, power: str, health: int):
        self.name = name
        self.power = power
        self.health = health
    

    # TODO: Define attack method and implement it
    def attack(self): 
        print(f"{self.name} attacks with {self.power}!")

    # TODO: Define heal method and implment it
    def heal(self):
        self.health += 10 
        print(f"{self.name} heals 10 points. New health: {self.health}.")
     

# TODO: Create superhero instance
superhero = SuperHero("Catwoman", "Agility", 120)


# TODO: Use the attack() and heal() method
superhero.attack() 
superhero.heal() 
