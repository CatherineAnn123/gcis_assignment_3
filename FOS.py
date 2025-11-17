"AJSAL MUHAMMED - 432004248"
menu={"Drinks":{"Cola": 5.0,"Juice": 7.0}," Entrees": {"Burger": 20.0,"Pizza": 25.0},
    "Sides": {"Fries": 8.0,"Salad": 10.0}}

class Order:
    __slots__=["__order_id","__combos","__total_amount"]
    def __init__(self,order_id):
        """Initialize  Order with  ID,  empty combo list,  zero total amount."""
        self.__order_id=order_id
        self.__combos=[]
        self.__total_amount=0
    def add_combo(self,combos):
        """Adds a Combo  and updates total using combos.get_total()."""
        self.__combos.append(combos)
        self.__total_amount+=combos.get_total()
    def display_reciept(self):
        """Print receipt showing all combos and the final total amount"""
        print(f"Reciept for Order Id :{self.__order_id}")
        print("-"*30)
        print("")
        print("-"*30)
        print(f"Total amount:{self.__total_amount}AED")

        
    
