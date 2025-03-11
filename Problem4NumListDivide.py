#by Medina Kubanychbekova
#03/11/2025

# Problem 4: Storing numbers divisible by 10 up to 50
tens = []  # Initialize empty list
counter = 0  # Start counter at 0

while counter <= 50:
    if counter % 10 == 0:  # Check if number is divisible by 10
        tens.append(counter)  # Append to list
    counter += 1  # Increment counter

print("Numbers divisible by 10 up to 50:", tens)  # Confirm list contents