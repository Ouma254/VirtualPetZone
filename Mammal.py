class Mammal:
    def animal_option(self):
        print("...MAMMAL PET...")
        global name_animal
        name_animal = input("Enter the name of the pet: ")
        print(f"Name: {name_animal}")

        print(f"Welcome you can check on the your {name_animal}")
        while True:
            print("\nCHOOSE OPTIONS")
            print("1. Feed/Store/Daily Use")
            print("2. Health Status")
            print("3. Production State")
            print("0. Quit Tests")

            choices = input("Enter Any of the above options to test")

            if choices == '1':
                mammal.feeding_habit()
            elif choices == '2':
                mammal.health()
            elif choices == '3':
                mammal.production()
            elif choices == '0':
                print("THANKS FOR CHOOSING THE SYSTEM")
                break
            else:
                print("Be Warned!! :(, wrong choice. Try Again")


    def perform_tests(self):
        pass


    def feeding_habit(self):
        feeds_supplied = {
            'silage': '100kg',
            'hay': '500 Tonnes',
            'Napier': '2 Tonnes'
        }
        print("The Available Feeds")
        print(feeds_supplied)
        print("In A Day the Pet Consumes: ")
        daily_consumption = {
            'silage': '10kg',
            'Napier': '10kg',
            'hay/Roughages': '2kg'
        }
        print("SUMMARY OF A DAILY CONSUMPTION")
        print(daily_consumption)

    def production(self):
        number_of_birth_yearly = int(input("Enter the number of times the Animal gets A calf"))
        print(f"{number_of_birth_yearly}")
        milk_production = {
            'Monday': 45,
            'Tuesday': 30,
            'Wednesday': 42,
            'Thursday': 39,
            'Friday': 40
        }
        monthly_milk = {
            'Week 1': 40,
            'Week 2': 37,
            'week 3': 40,
            'Week 4': 36
        }
        print("the daily milk production is :")
        print(milk_production)
        print("The monthly milk production: ")
        print(monthly_milk)



    def health(self):
        global weight
        weight = int(input("Enter the Weight of Animal"))

        if weight > 80 & 100 >= weight:
            print(f"SEEM the pet is Doing cool feeding program employed fits the Animal")
            print(f"Weight {weight} Kgs")

        elif weight > 50 & 80 >= weight:
            print(f"The pet lacks some body building to boost on the regeneration body cells for growth")
            print("We Recommend..")
            recommandations = {
                'body_building': ['Napier Grass', 'Silage'],
                'fat_feed': ['Silage', 'Hay', 'salt lick'],
                'water': 'clean water'
            }
            print(recommandations)
        else:
            print("Animal pet needs a Veterian")


mammal = Mammal()