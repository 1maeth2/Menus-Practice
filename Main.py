# create your menu below!


def meters_to_yards():
    while True:
        try:
            a = int(input("Enter A Distance(M): "))
            print(f"{a} meters converts to {a*1.094} yards")
        except ValueError:
            print("Please Enter A Valid Input")


def kilograms_to_pounds():
    while True:
        try:
            a = int(input("Enter A Weight(KG): "))
            print(f"{a} kg converts to {a*2.205} pounds")
        except ValueError:
            print("Please Enter A Valid Input")


def celcius_to_fahrenheit():
    while True:
        try:
            a = int(input("Enter A Temperature(C): "))
            print(
                f"{a} degrees celcius converts to {(a*9/5)+32} degrees fahrenheit"
            )
        except ValueError:
            print("Please Enter A Valid Input")


def kmph_to_mph():
    while True:
        try:
            a = int(input("Enter A Speed(KM/H): "))
            print(f"{a} KM per hour converts to {a*1.609} miles pre hour")
        except ValueError:
            print("Please Enter A Valid Input")


def createMenu(title, *menu):
    print(title.center(40, "-").upper())
    print(f"1. {menu[0]}")
    print(f"2. {menu[1]}")
    print(f"3. {menu[2]}")
    print(f"4. {menu[3]}")
    print("5. Exit")

    while True:
        try:
            a = int(input("Pick An Option Number (1-5): "))
            if (a <= 5):
                return a
            else:
                print("Please Enter An Valid Option Number")
        except ValueError:
            print("Please Enter A Valid Input")


selection = createMenu("MENU", "Meters to Yards", "Kilograms to Pounds",
                       "Celsius to Fahrenheit",
                       "Kilometres per hour to miles per hour")

if selection == 1:
    meters_to_yards()
elif selection == 2:
    kilograms_to_pounds()
elif selection == 3:
    celcius_to_fahrenheit()
elif selection == 4:
    kmph_to_mph()
elif selection == 5:
    print("Exiting....")
