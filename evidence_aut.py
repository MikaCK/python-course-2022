class Auto:
    def __init__(self, car_licence_plate, make_type_vehicle,number_km):
        self.car_licence_plate = car_licence_plate
        self.make_type_vehicle = make_type_vehicle
        self.number_km =number_km
        self.is_car_free = True

    def rent_car(self):
        if self.is_car_free == True:
            self.is_car_free = False
            return f"I confirm the rental of the vehicle."
        else:
            return f"The vehicle is not available."
    
    def get_info(self):
        return f"The car info is: type - {self.make_type_vehicle}, register number - {self.car_licence_plate}"

def renting_a_car(user_choice:str):
    if user_choice == "Peugeot":
        print(peugeout.get_info())
        print(peugeout.rent_car())
    elif user_choice == "Skoda":
        print(skoda.get_info())
        print(skoda.rent_car())
    else:
        print("This type of vehicle is not available")


# Agency has two cars and they are free
peugeout = Auto('4A2 3020', 'Peugeot 403 Cabrio', 47534)
skoda = Auto('1P34747', 'Skoda Octavia', 41253)

# Ask user what he wants:
user_choice_input = input('What car do you want to rent?(Peugeot/Skoda): ')
renting_a_car(user_choice_input)

#Ask another user what he wants:
print("-------------------")
user_choice_input = input('What car do you want to rent?(Peugeot/Skoda): ')
renting_a_car(user_choice_input)

