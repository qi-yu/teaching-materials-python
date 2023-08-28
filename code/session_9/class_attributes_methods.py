# ----- 1. Define a class: -----
class House:
    """
    A simple "House" class.
    """

    # Define class attributes:
    general_info = "This is a house."
    blueprint_creator = "NN"

    # Define class methods:
    @classmethod
    def send_greeting_message(cls):
        print("Hello world. I'm a house.")

    @classmethod
    def modify_blueprint_creator(cls, name): # name = "Max M."
        House.blueprint_creator = name

# ----- 2. Construct instances of the class: -----
first_house = House()
second_house = House()


# ----- 3. Access the class attributes -----
## Access the attribute from the class:
# print(House.general_info)
# print(House.blueprint_creator)

## The attribute can also be accessed from instances:
# print(first_house.general_info)
# print(second_house.blueprint_creator)

# ----- 4. Access class methods -----
## 4.1 Access the method from the class:
# House.send_greeting_message()

print("Current blueprint creator name: ", House.blueprint_creator)
House.modify_blueprint_creator("Max Mustermann")
print("Modified blueprint creator name: ", House.blueprint_creator)

### Note that the blueprint creator name of all instances
### are also changed correspondingly:
print(first_house.blueprint_creator)
print(second_house.blueprint_creator)

## 4.2 Access the method from instances:
# first_house.send_greeting_message()
# first_house.modify_blueprint_creator("Erika Mustermann")
# print(first_house.blueprint_creator)

### Note that even if we only accessed the method from one instance (first_house),
### The value of "blueprint_creator" is changed for all instances of the class,
### because "blueprint_creator" is a class attribute.
# print(second_house.blueprint_creator)

