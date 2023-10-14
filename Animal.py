"""
this is animal class
in here we discuss the attributes && behaviors
"""
class Animal:
    # the animal attributes
    # def __int__(self, *args):
    #     self.type = type.args

    # the behaviors of the animals
    def mode_movement(self):
        pass
        # global leg
        # global leg_type = True
        # wings = True

    def feeding_mode(self):
        pass

    def reproduction_period(self):
        pass

    def health_state(self):
        pass

    def main(self):
        ani = Animal()


        while True:
            print("\nOptions to Choose")
            print("1. Bird Pets")
            print("2. Mammal Pets")
            print("0. Exit")

            choice = input("Enter your selection:")

            if choice == '1':
                ani.mode_movement()
            elif choice == '2':
                ani.feeding_mode()
            elif choice == '0':
                print("Thank you for using the Virtual Pet System, Bye")
                break
            else:
                print("Invalid Choice, Try again")





