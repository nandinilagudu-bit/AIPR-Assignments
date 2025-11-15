class ShoppingCart:
    def __init__(self):
        self.items = []  # each item is {"name": , "price": }
    
    def add_item(self, name, price):
        # Validate name
        if not isinstance(name, str) or name.strip() == "":
            return "Invalid input"
        
        # Validate price
        if not isinstance(price, (int, float)) or price < 0:
            return "Invalid input"
        
        self.items.append({"name": name, "price": price})
        return "Item added"
    
    def remove_item(self, name):
        # Validate name
        if not isinstance(name, str) or name.strip() == "":
            return "Invalid input"
        
        # Search and remove
        for i, item in enumerate(self.items):
            if item["name"] == name:
                self.items.pop(i)
                return "Item removed"
        
        return "Item not found"
    
    def total_cost(self):
        return sum(item["price"] for item in self.items)
cart = ShoppingCart()

print("\n--- Add Item Tests ---")
print(cart.add_item("Apple", 30))        # valid
print(cart.add_item("Milk", 55.5))       # valid
print(cart.add_item("Pen", 10))          # valid
print(cart.add_item("", 20))             # invalid
print(cart.add_item("Bag", -30))         # invalid
print(cart.add_item("Shoes", "100"))     # invalid

print("\n--- Remove Item Tests ---")
print(cart.remove_item("Pen"))           # valid
print(cart.remove_item("Pen"))           # already removed
print(cart.remove_item(""))              # invalid
print(cart.remove_item(123))             # invalid
print(cart.remove_item("Phone"))         # not found

print("\n--- Total Cost Test ---")
print("Total Cost =", cart.total_cost())  # Apple + Milk
