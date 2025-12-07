import random

while True:
    try:
        number_of_dices = int(input('How many dices? '))
        break
    except ValueError:
        print("Error: Please enter a valid whole number. Try again.")

result = 0

for i in range(number_of_dices): 
    result += random.randint(1, 6)


print('Total Result: ', result)
