# Exercise 1: OOP Shopping Cart

class Cart():
        def __init__(self, customer_name):
            self.customer_name = customer_name
            self.cart = []

        def add_to_cart(self, x):
            self.cart.append(x.lower())
            print(f"{x.title()} added to your cart.")

        def remove_from_cart(self, x):
            if x in self.cart:
                self.cart.remove(x)
                print(f"{x.title()} removed from your cart.")
            else:
                print(f"{x.title()} is not in your cart!")

        def show_cart(self):
            if self.cart:
                print(f"{self.customer_name.title()}'s cart:")
                for item in self.cart:
                    print(item.title())
            else:
                print(f"{self.customer_name.title()}'s cart is empty.")

def run():
    customer_name = input("Welcome. What is your name? ")
    my_cart = Cart(customer_name)
    while True:
        ask = input("What would you like to do? (A)dd/(R)emove/(S)how/(Q)uit ").lower()
        if ask == 'q':
            break
        elif ask == 'a':
            item = input("What would you like to add? ")
            my_cart.add_to_cart(item)
        elif ask == 's':
            my_cart.show_cart()
        elif ask == 'r':
            item = input("What would you like to remove? ")
            my_cart.remove_from_cart(item)
        else:
            print("Invalid input.")
run()

# Exercise 2: Animal class
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
            print(f"\n{self.name.title()} the {self.species.title()} played a tough round of {self.species} chess.")
            print(f"Their energy fell to {self.energy}.")

cecilia = Animal("cecilia", "baboon")

cecilia.eat(2)
cecilia.sleep(4)
cecilia.play()
