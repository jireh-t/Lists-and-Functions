""" A programme to record data about absences in a workplace"""


def int_checker(question):
    error = "Please enter an integer"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


# Gets input for each person's name and number of days absent
def get_info():
        name = ""
        absences = []

        # Have an easy escape key
        while name != "$":
            name = input("Enter name: ")

            # Test if there was enough information entered
            if name == "$":
                if len(absences) > 0:
                    average_days(absences)
                    break
                # If the list is empty
                else:
                    print("There was no data entered. Good bye!")
                    break

            # Make sure the days is an integer
            days = int_checker("Enter the number of absence days: ")
            print()
            absences.append([name, days])


# Calculates the average number of absence days per year
def average_days(absences):
    length = len(absences)
    total = 0

    for people in absences:
        total += people[1]

    ave_day = total/length
    print()
    print(f"The average number of staff absence days was {ave_day:.2f} days")



# Main
get_info()




