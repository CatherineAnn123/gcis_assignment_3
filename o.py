menu={"Drinks":{"Cola": 5.0,"Juice": 7.0}," Entrees": {"Burger": 20.0,"Pizza": 25.0},
    "Sides": {"Fries": 8.0,"Salad": 10.0}}
class combo:
     __slots__ = ["__drink", "__entree", "__sides", "__total_price"]
     
     def __init__(self, drink, entree, sides):
          self.__drink=drink
          self.__entree=entree
          self.__sides=sides
          self.__total_price=0
          if self.__drink in menu["Drinks"].keys():
               self.__total_price += menu["Drinks"][self.__drink]
          else:
              self.__drink = None
          if self.__entree in menu[" Entrees"].keys():
               self.__total_price += menu[" Entrees"][self.__entree]
          else:
               self.__total_price=None
          if self.__sides in menu["Sides"].keys():
               self.__total_price += menu["Sides"][self.__sides]
          else:
               self.__total_price=None
     
     def get_total(self):
          return self.__total_price
     def __str__(self):
          return f"Drink: {self.__drink} | Entrée: {self.__entree} | Side: {self.__sides} | Combo Price: {self.__total_price} AED"
     def display_combo(self):
          print("Combo Details:")
          print(f"Drink: {self.__drink} | Entree: {self.__entree} | Side: {self.__sides}")
          print(f"Total combo price: {self.get_total()} AED ")

class Order:
    __slots__=["__order_id","__combos","__total_price"]
    def __init__(self,order_id):
        """Initialize  Order with  ID,  empty combos list,  zero total amount."""
        self.__order_id=order_id
        self.__combos=[]
        self.__total_price=0
    def add_combo(self,combos):
        """Adds a Combo  and updates total using combos.get_total()."""
        self.__combos.append(combos)
        self.__total_price += combos.get_total()
    def get_total(self):
           return self.__total_price
    def display_receipt(self):
        """Print receipt showing all combos and the final total amount"""
        print(f"Reciept for Order Id :{self.__order_id}")
        print("-"*30)
        count = 1          
        for combos in self.__combos:
            print(f"Combo {count}:")
            print(combos)   
            print("-" * 30)
            count += 1 
        print("-"*30)
        print(f"Total amount:{self.get_total()}AED")
    def main():
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
        combo1 = combo(drink, entree, side)
        order.add_combo(combo1)
        combo1.display_combo()
        print("\n\nOrder successfully created!\n")
        order.display_reciept()   
    main()

   

combo1 = combo("Cola", "Burger", "Fries")
combo1.display_combo()
order1 = Order(101)
combo2= combo("Juice","Pizza","Salad")
order1.add_combo(combo1)
order1.add_combo(combo2)
order1.display_receipt()





        
    


                         
          