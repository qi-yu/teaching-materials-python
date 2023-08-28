# ----- 1. Define a class: -----
class House:
    # Define class attributes:
    general_info = "This is a house."
    blueprint_creator = "NN"
    current_year = 2023

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
first_house = House()
second_house = House()

# print("Blueprint creator: ", House.blueprint_creator)
# first_house.send_greeting_message()

# ----- 3. Examples of calling instance methods: -----
first_house.set_wall_color("white")
first_house.set_year_of_build(1998)

second_house.set_wall_color("pink")
# second_house.set_year_of_build(2011)

## Check the values of the instance attributes:
print(first_house.get_wall_color())
print(second_house.get_wall_color())
# print("Age of the first house: ", first_house.get_age())
# print("Age of the second house: ", second_house.get_age())

## You can also access the attributes directly,
## instead of calling the get_wall_color() method:
print(first_house.wall_color)
print(second_house.wall_color)