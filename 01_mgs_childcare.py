children = []
COST = 12


def drop_off():
    child = input("Name of child: ")
    children.append(child)
    print(f"{child} has been dropped off and added to the list")
    print()


def pick_up():
    child = input("Name of child: ")
    if child in children:
        children.remove(child)
        print(f"{child} has been picked up and removed from the list")
        print()

    else:
        print(f"{child} is not in the list, please check that you have "
              f"spelt the name correctly")
        print()


def calc_cost():
    hours = int(input("How many hours to charge? "))
    num = len(children)
    total = hours * num * COST
    print(f"The total charge for {num} children and {hours} hours is ${total}")
    print()


def print_roll():
    for people in children:
        print(people)


def main():
    choice = 0
    while choice != 5:
        print("---------------------------------")
        print("Welcome to MGS Childcare")
        print("Please select one of the items below")
        print()
        print("1 Drop off a child")
        print("2 Pick up a child")
        print("3 Calculate cost")
        print("4 Print roll")
        print("5 Exit the system")
        print("----------------------------------")
        choice = int(input("Enter your choice (number between 1 and 5): "))
        print()

        if choice == 1:
            drop_off()

        elif choice == 2:
            pick_up()

        elif choice == 3:
            calc_cost()

        elif choice == 4:
            print_roll()

        elif choice == 5:
            return("Goodbye")

        else:
            print("Please select a number between 1 and 5")


print(main())
