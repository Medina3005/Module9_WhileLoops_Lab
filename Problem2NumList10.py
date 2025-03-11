#by Medina Kubanychbekova
#03/11/2025
# Problem 2: Creating a list from 0 to 10 using a while loop
L = []  # Initialize an empty list
counter = 0  # Start counter at 0

while counter <= 10:
    L.append(counter)  # Append current counter value to the list
    counter += 1  # Increment counter

print("List from 0 to 10:", L)  # Confirm list contents