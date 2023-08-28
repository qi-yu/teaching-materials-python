# ----- 1. Define a class: -----
class House:
    """
    A simple "House" class.
    """
    info = "This is a house." # The class "House" has an attribute "info"


# ----- 2. Construct instances of the class: -----
# This is done by calling the class name with a "()" behind it.
first_house = House()
second_house = House()


# ----- 3. Access the attribute "info" from the Class -----
print(first_house.info)
print(second_house.info)
print(House.info)
