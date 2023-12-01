#the list of gifts in the bag
gifts = ["an Apple", "a Cake", "a Chocolate box", "a toy", "a story book", "a visa"]

#getting the user selected number
input_number = int(input("Enter a number from 0 to 5 to get an item from the gift bag\n"))

#printing out the item picked
if input_number >= 0 and input_number <= 5:
    print(f"You got {gifts[input_number]}")
else:
    print("Enter a valid number")