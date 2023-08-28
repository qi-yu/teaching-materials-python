class House:
    # Define class attributes:
    general_info = "This is a house."
    blueprint_creator = "NN"
    current_year = 2023
    blueprint_usage_count = 0 # Count how many times the blueprint has been used,
                              # i.e., how many instances of this class has been constructed

    def __init__(self, color, year, has_heating, address):
        House.blueprint_usage_count += 1
        self.wall_color = color
        self.year_of_build = year
        self.has_heating = has_heating
        self.address = address

    # Define class methods:
    @classmethod
    def send_greeting_message(cls):
        print("Hello world. I'm a house.")

    @classmethod
    def modify_blueprint_creator(cls, name):
        House.blueprint_creator = name

    # Define instance methods:
    def set_wall_color(self, color):
        self.wall_color = color

    def get_wall_color(self):
        return self.wall_color

    def set_year_of_build(self, year):
        self.year_of_build = year

    def get_age(self):
        age = House.current_year - self.year_of_build
        return age

# ----- 2. Construct instances of the class: -----
## Note that the arguments of the constructors
## can be passed in both named or unnamed way
first_house = House(color="white",
                    year=1998,
                    has_heating=False,
                    address="Maple Street 1")

# second_house = House("yellow", 2011, True, "Maple street 20")

# print("Age of the first house:", first_house.get_age())
# print("Age of the second house:", second_house.get_age())
# print()

# print("Address of the first house:", second_house.address)
# print("What wall color does the first hacve?", second_house.wall_color)
# print("Does the first second has heating?", first_house.has_heating)

## You can still re-write the value of the instance attributes using instance methods:
print("Wall color of the second house:", first_house.wall_color)
first_house.set_wall_color("pink")
print("Wall color of the second house:", first_house.wall_color)
