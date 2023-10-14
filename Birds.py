from Animal import Animal
from Mammal import Mammal


# the bird class inherits the Class Animal & Implements
class Birds(Animal, Mammal):

    def __init__(self, type, name,):
        self.type = type
        self.name = name

    def naming_pet(self):
        global name
        global pets
        global type

        pet = []
        name = input("Enter the name of the Pet: ")
        print(f"{name}")

        while True:
            print("\nChoose on the choice to Test of the pet Above")
            print("1. Feeding Habits")
            print("2. Weight of Animal")
            print("3. Production Rate")
            print("4. Health Status")
            print("0. Quit")

            user_choice = input("Test the pet: ")
            if user_choice == '1':
                bird.feeding_mode()
            elif user_choice == '2':
                bird.weight()
            elif user_choice == '3':
                bird.reproduction_period()
            elif user_choice == '4':
                bird.health_state()
            elif user_choice == '0':
                print(f"Keep Monitoring on your {name}")
            else:
                print("Warning!! Invalid choice")


    def control_unit(self):

        while True:
            print("<<<...Welcome to the Virtual Pet Monitor System...>>>")
            print("\n Choose Options")
            print("1. Bird")
            print("2. Mammal")
            print("0. Exit")

            choice = input("Enter the type of Pet:")

            if choice == '1':
                bird.naming_pet()
            elif choice == '2':
                bird.animal_option()
            elif choice == '0':
                print("Thank You for Using the VIRTUAL PET MONITOR")
                print("Bye :)")
                break
            else:
                print("Error!! Wrong Choice, Try Again")




    def mode_movement(self):
        print("")

    def feeding_mode(self):
        print(f"{type} feeds by peckings")

    def reproduction_period(self):
        number_of_eggs = int(input("Enter the number of eggs the bird lays in a week/month: "))
        if number_of_eggs >= 5:
            print("the bird is correct state of production")

        elif number_of_eggs == 3 & number_of_eggs == 2 & number_of_eggs == 1:
            print(" The bird have a poor habit of production ")
            print("And the suggestion to recommend this is to:\n feed the bird layers mash\nalso check the birds health status")

    def health_state(self):
        weight = int(input("Recent weight: "))
        if weight >= 20:
            print("healthy birds should way above 25Kgs")

        elif weight < 20 & weight == 0:
            print(f"the pet is under-weight needs to checked up as it is under weight")

        else:
            print("error!! ")

    def weight(self):
        pass

    # def animal_option(self):
    #     print()
    #


bird = Birds("animal", "bird")
bird.control_unit()
