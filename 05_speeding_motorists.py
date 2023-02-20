"""Program to keep track of speeding tickets, and alert the officer if an
outstanding warrant to arrest the speeder"""


def int_checker(question):
    error = "Please enter an integer"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


# Function to ask the user their name and amount over speed limit
def get_details():
    name = ""
    speeding = []  # 2 dimensional list
    total_fines = 0  # Count to keep track of fines
    total = 0

    while name != "X":  # Have an easy escape key
        name = input("Enter name of speeder: (Enter 'X' to stop) ").title()

        # Test if there was enough information entered
        if name == "X":
            if len(speeding) > 0:
                break
            else:  # If the list is empty
                print("There was no data entered. Good bye!")
                break

        # Check if person is wanted for arrest
        if name == "James Wilson" or name == "Helga Norman" or name == \
                "Zachary Conroy":
            print(f"{name.upper()} - WARRANT TO ARREST")

        # Make sure the days is an integer
        over = int_checker("Enter the amount over speed limit: ")
        print()
        speeding.append([name, over])
        fine = fine_calc(over)
        print(f"{name} to be fined ${fine}")
        print()
        total_fines += 1  # Keep track of fines
        total += fine

    print()
    print(f"Total fines: {total_fines}")

    # Print out the names and amounts
    for people in speeding:
        print(f"{speeding.index(people) + 1}) Name: {people[0]}  Amount Over "
              f"Limit:"
              f" {people[1]}")
        print(f"Amount Over Limit: {people[1]}")
    print(f"Total amount of fines: ${total}")


# Function to calculate the fine
def fine_calc(over):
    if over < 10:
        fine = 30
    elif over < 15:
        fine = 80
    elif over < 20:
        fine = 120
    elif over < 25:
        fine = 170
    elif over < 30:
        fine = 230
    elif over < 35:
        fine = 300
    elif over < 40:
        fine = 400
    elif over < 45:
        fine = 510
    else:
        fine = 630

    return fine


# Main
get_details()
