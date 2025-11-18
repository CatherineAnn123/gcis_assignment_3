class Combo:
    __slots__ = ["drink", "entree", "side", "total_price"]

    def __init__(self, drink, entree, side):
        self.drink = drink
        self.entree = entree
        self.side = side
        self.total_price = 0    

        if self.drink:
            self.total_price += menu["Drinks"][self.drink]
        if self.entree:
            self.total_price += menu["Entrees"][self.entree]
        if self.side:
            self.total_price += menu["Sides"][self.side]   

    def get_total(self):
        return self.total_price
