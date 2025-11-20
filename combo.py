menu={"Drinks":{"Cola": 5.0,"Juice": 7.0}," Entrees": {"Burger": 20.0,"Pizza": 25.0},
    "Sides": {"Fries": 8.0,"Salad": 10.0}}
class Combo:
    __slots__ = ["drink", "entree", "side", "total_price"]

    def __init__(self, drink, entree, side):
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
        print("\n\nCombo Details:")
        print(f"Drink: {self.drink} | Entree: {self.entree} | Side: {self.side}")
        print(f"Total combo price: {self.total_price}")

    def get_total(self):
        return self.total_price


class Order:
    __slots__=["__order_id","__combo","__total_amount"]
    def __init__(self,order_id):
        """Initialize  Order with  ID,  empty combo list,  zero total amount."""
        self.__order_id=order_id
        self.__combo=[]
        self.__total_amount=0
    def add_combo(self,combo):
        """Adds a Combo  and updates total using combos.get_total()."""
        self.__combo.append(combo)
        self.__total_amount+=combo.get_total()
    def display_reciept(self):
        """Print receipt showing all combos and the final total amount"""
        print(f"Reciept for Order Id :{self.__order_id}")
        print("-"*30)
        print("")
        print("-"*30)
        print(f"Total amount:{self.__total_amount}AED")
combo1 = Combo("Cola", "Burger", "Fries",)
combo1.display_combo()
order1 = Order(101)
order1.add_combo(combo1)
order1.display_reciept()

