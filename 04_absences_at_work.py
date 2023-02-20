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
    absences = []  # 2 dimensional list

    # Have an easy escape key
    while name != "$":
        name = input("Enter name: ")

        # Test if there was enough information entered
        if name == "$":
            if len(absences) > 0:
                average_days(absences)
                most_least_absence(absences)
                break
            else:  # If the list is empty
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

    global ave_day
    ave_day = total/length
    print()
    print(f"The average number of staff absence days was {ave_day:.2f} days")
    print()


# Calculate which staff member had the most absences
def most_least_absence(absences):
    absence_days = []  # Make a new list so I can find the maximum
    for days in absences:
        absence_days.append(days[1])

    most = max(absence_days)  # Find most days absent

    # Find the corresponding staff member
    index = absence_days.index(most)
    print(f"The person with the most days absent was {absences[index][0]} "
          f"with {most} days")
    print()

    # Find how many staff were absent for 0 days
    zero_indices = []

    # Check how many times 0 appears in the list
    for num in range(len(absence_days)):
        if absence_days[num] == 0:
            zero_indices.append(num)

    # Find the corresponding names
    print("List of people with no absences:")
    for indexes in zero_indices:
        print(f"{absences[indexes][0]}")
    print()

    above_average = []

    # Check how many people had above average absences
    for nums in range(len(absence_days)):
        if absence_days[nums] > ave_day:
            above_average.append(nums)

    # Find the corresponding names
    print("List of people absent above average:")
    for indes in above_average:
        print(f"{absences[indes][0]} with {absences[indes][1]} days")
    print()


# Main
get_info()
