import random

print('Guess game!')
print('Guess the number in range 1 - 1000')

value = random.randrange(1, 1000)
user_value = -1
steps = 0

while user_value != value:
    user_value = int(input('Provide a value: '))
    steps += 1
    if user_value < value:
        print('Nope, you are looking for higher value.')
    elif user_value > value:
        print('Nope, you are looking for lower value.')

print(f"Congrats! You've managed to find number {value} in {steps} steps.")