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
