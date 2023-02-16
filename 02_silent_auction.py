item = input("What is the auction for? ")
price = float(input("What is the reserve price? "))
highest = 0

print()
print(f"The auction for the {item} has started!")
print("To end the auction please enter a bid price of -1")
print()

# loop to terminate the auction when user enters -1
while True:
    print(f"Highest bid so far is ${highest}")
    bid = float(input("What is your bid? "))
    print()

    # store the bid if it is more than the highest amount
    if bid > highest:
        highest = bid
    elif bid == -1:
        break
    else:
        print("Need a higher bid")
        print()

# tell the user if the item has sold or not
if highest > price:
    print(f"The auction for the {item} finished with a bid of ${highest}")

else:
    print(f"Sorry, the {item} did not sell")


