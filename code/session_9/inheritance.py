class Furniture:
    count = 0

    def __init__(self, material, price, seller_names):
        Furniture.count += 1
        self.material = material
        self.price = price
        self.sellers = seller_names

    def set_new_price(self, new_price):
        self.price = new_price

    def set_seller(self, sellers):
        self.sellers = sellers

    def get_price(self):
        return self.price


class Desk(Furniture):
    def info(self):
        print("This is a desk.")

    def set_drawer_numbers(self, num):
        self.drawer_numbers = num

    def get_drawer_numbers(self):
        return self.drawer_numbers

class Adjustable_Desk(Desk):
    def info(self):
        print("This is an adjustable desk.")  # Note the overriding here!

    def set_height_range(self, min, max):
        self.min_height = min
        self.max_height = max

    def get_height_range(self):
        print("Minimum height:", str(self.min_height) + "m", "; Maximum height:", str(self.max_height) + "m")

# ----- 1. Construct an instance of the grandchild-class "Adjustable_Desk" -----
my_adjustable_desk = Adjustable_Desk(material="wood", price="300 EUR", seller_names=["Obi", "Ikea"])

## Set some instance attributes:
my_adjustable_desk.set_height_range(1, 1.5)
my_adjustable_desk.get_height_range()

# ----- 2. Showcases of inheritance: -----
# Note that my_adjustable_desk can also access the methods in the parent-class "Desk",
# and also those from the grandparent-class "Furniture"
# my_adjustable_desk.set_drawer_numbers(2)
# print(my_adjustable_desk.get_drawer_numbers())
#
# print("Price: ", my_adjustable_desk.get_price())
# my_adjustable_desk.set_new_price("200 EUR")
# print("New price: ", my_adjustable_desk.get_price())

