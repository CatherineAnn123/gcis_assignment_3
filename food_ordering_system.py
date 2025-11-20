# GCIS ASSIGNMENT 3

# GROUP-6:
# Catherine Fernandez (413001100)
# Ajsal Muhammed Kizhakkepattuthody (432004248)

# MANIFESTO:
# task 2,4 - Catherine Fernandez
# task 1,3 - Ajsal Muhammed Kizhakkepattuthody


# task-1
menu = {"Drinks":{"Cola": 5.0,"Juice": 7.0},"Entrees": {"Burger": 20.0,"Pizza": 25.0},
    "Sides": {"Fries": 8.0,"Salad": 10.0}}

# task-2
class Combo:
    __slots__ = ["drink", "entree", "side", "total_price"]

    def __init__(self, drink, entree, side):
        """
        Initialize Combo with drink, entree, side, and total price
        
        Parameters:
          drink (str) : drink input
          entree (str) : entree input
          side (str) : side input
          
        """
        self.drink = drink
        self.entree = entree
        self.side = side
        self.total_price = 0    

        if self.drink in menu["Drinks"].keys() :
            self.total_price += menu["Drinks"][self.drink]
        else:
            self.drink = None
        if self.entree in menu["Entrees"].keys():
            self.total_price += menu["Entrees"][self.entree]
        else:
            self.entree = None
        if self.side in menu["Sides"].keys():
            self.total_price += menu["Sides"][self.side]   
        else:
            self.side = None
    
    def display_combo(self):
        """
        Prints combo details
        """
        print("\n\nCombo Details:")
        print(f"Drink: {self.drink} | Entree: {self.entree} | Side: {self.side}")
        print(f"Total combo price: {self.total_price}")

    def get_total(self):
        """
        Returns: 
          get_total (float) : total price of the combo
        """
        return self.total_price

# task-3
class Order:
    __slots__=["__order_id","__combos","__total_amount"]

    def __init__(self,order_id):
        """
        Initialize Order with ID, empty combo list, zero total amount

        Parameter:
            order_id (int) : unique id for each order
        """
        self.__order_id=order_id
        self.__combos=[]
        self.__total_amount=0

    def add_combo(self,combo):
        """
        Adds a Combo and updates total using combos.get_total()

        Parameter:
          combo (Combo) : combo to add
        """
        self.__combos.append(combo)
        self.__total_amount+=combo.get_total()

    def display_reciept(self):
        """
        Print a receipt showing all combos and the final amount
        """
        print(f"Reciept for Order Id :{self.__order_id}\n")
        print("-"*30)
        print(f"\nTotal amount: {self.__total_amount} AED\n")
        print("-"*30)

# task-4
def main():
    """
    This function prints a welcome message followed by the menu.
    Adds user input to let customers choose items from the menu, and creates the order accordingly.
    After the order is created, it displays the receipt.
    """
    
    print("\n--- Welcome to Eat and Drink ---")
    print("\nToday's Menu:")

    for i in menu:
        for item, price in menu[i].items():
            print(f"{item} - {price} AED")

    print("\n\nCreate your combo:\n")
    
    drink = input("Enter drink: ").title()
    entree = input("Enter entree: ").title()
    side = input("Enter side: ").title()

    order = Order(101)
    combo1 = Combo(drink, entree, side)
    order.add_combo(combo1)
    combo1.display_combo()

    print("\n\nOrder successfully created!\n")
    order.display_reciept()   


if __name__ == "__main__":
    main()





        
    


                         
          
