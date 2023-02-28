class Cart():
        def __init__(self, customer_name):
            self.customer_name = customer_name
            self.cart = []

        def add_to_cart(self):
            pass

        def remove_from_carT(self):
            pass

        def show_cart(self):
            pass

def run():
    customer_name = input("Welcome. What is your name? ")
    my_cart = Cart(customer_name)
    while True:
        ask = input("What would you like to do? Add/Remove/Show/Quit ").lower()
        if ask == 'quit':
            break
        elif ask == 'add':
            item = input("What would you like to add? ")
            my_cart.add_to_cart(item)


# Animal class
class Animal:

        def __init__(self, name, species, energy=10):
            self.name = name
            self.species = species
            self.energy = energy

        def eat(self, x):
            self.energy += 1*x
            print(f"\n{self.name.title()} the {self.species.title()} ate {x} {self.species} food.")
            print(f"Their energy rose to {self.energy}!")

        def sleep(self, x):
            self.energy += 2*x
            print(f"\n{self.name.title()} the {self.species.title()} took a {x}-hour {self.species} nap.")
            print(f"Their energy rose to {self.energy}!")

        def play(self):
            self.energy -= 2
            print(f"\n{self.name.title()} the {self.species.title()} played some {self.species} games.")
            print(f"Their energy fell to {self.energy}.")

cecilia = Animal("cecilia", "baboon")

cecilia.eat(2)
cecilia.sleep(4)
cecilia.play()
