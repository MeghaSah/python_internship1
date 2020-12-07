# COFFEE MACHINE PROGRAM

class CoffeeMachine:
    running = False
    print("Welcome to coffee spot")

#function for initialization
    def __init__(self, water, milk, coffee, money):
        # default quanitities
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money

        #if the machine isnt running then start running
        if not CoffeeMachine.running:
            self.start()

#function where main program starts
    def start(self):
        self.running = True
        self.action = input("Write action (buy, fill, take, report, off):\n")
        print()
        #possible choices to perform in the coffee machine
        if self.action == "buy":
            self.buy()
        elif self.action == "fill":
            self.fill()
        elif self.action == "take":
            self.take()
        elif self.action == "off":
            exit()
        elif self.action == "report":
            self.status()



#return back to main function after the process
    def return_to_menu(self):
        print()
        self.start()

    def available_check(self):
        self.not_available = ""
        if self.water - self.reduced[0] < 0:
            self.not_available = "water"
        elif self.milk - self.reduced[1] < 0:
            self.not_available = "milk"
        elif self.coffee - self.reduced[2] < 0:
            self.not_available = "coffee"

        if self.not_available != "":
            print(f"Sorry,there is not enough {self.not_available}!")
            return False
        else:
            print("Preparing your coffee!")
            print()
            print("remaining product")
            self.status()
            return True

    def deduct_supplies(self):
        self.water -= self.reduced[0]
        self.milk -= self.reduced[1]
        self.coffee -= self.reduced[2]
        self.money += self.reduced[3]



    def buy(self):
        self.choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if self.choice == '1':
            self.reduced = [200, 100, 15, 4] #value 0f water, milk, coffee, money
            if self.available_check(): # checkimg whether the supplies are available
                self.deduct_supplies() # reducing supply value

        elif self.choice == '2':
            self.reduced = [200, 100, 20, 7]
            if self.available_check():
                self.deduct_supplies()

        elif self.choice == "3":
            self.reduced = [200, 100, 10, 6]
            if self.available_check():
                self.deduct_supplies()

        elif self.choice == "back":
            self.return_to_menu()

        self.return_to_menu()


    def fill(self):
        self.water += int(input("how many ml of water do you want to add:\n"))
        self.milk += int(input("how many ml of milk do you want to add:\n"))
        self.coffee += int(input("how many grams of coffee beans do you want to add:\n"))
        self.return_to_menu()

# for taking the money from the machine
    def take(self):
        print(f"I gave you ${self.money}")
        self.money -= self.money
        self.return_to_menu()

 # to display the quantities of supplies
    def status(self):
        print(f"The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee} of coffee beans")
        print(f"${self.money} of money")
        self.return_to_menu()


# quantities for initialization

CoffeeMachine(400, 540, 120, 550)


