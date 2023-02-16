"""Keep track of details for a taxi company"""

BASE_FEE = 10

total_time = 0
total_income = 0
trips = 0

name = input("What is your name? ")
choice = input("Would you like to start a new trip? ('yes' or 'no') ").lower()
print()

# Keep asking the user for trips until 'no' is entered
while choice != "no":
    if choice == "yes":
        time = int(input("How long was the trip in minutes? "))
        print()
        total_time += time

        cost = BASE_FEE + 2 * time
        print(f"The cost for that trip was ${cost}")
        print()
        total_income += cost

        trips += 1

        choice = input("Would you like to start a new trip? ('yes' or 'no') ").lower()
        print()

    # Ask the user again if yes or no is not entered
    else:
        print("Please enter 'yes' or 'no'")
        choice = input("Would you like to start a new trip? ('yes' or 'no') ").lower()
        print()

# Calculate the average
average_time = total_time / trips
average_cost = total_income/ trips

# Display all the details for the user
print(f"The name of the driver was {name}")
print(f"The total time of all trips was {total_time} minutes")
print(f"The average time of all trips was {average_time:.1f} minutes")
print(f"The total income of all trips was ${total_income}")
print(f"The average cost of all trips was ${average_cost:.2f}")


