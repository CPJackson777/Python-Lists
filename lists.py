import random
"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))
    
# Print the my_randoms list
print(f'my_random {my_randoms}')

# Generate a list of numbers 1..10
numbers_1_to_10 = range(1, 11)

# Iterate from 1 to 10
for number in numbers_1_to_10:
    the_numbers_match = False

    # Iterate your random number list here
    for randomNumber in my_randoms:
        if randomNumber == number:
            the_numbers_match = True
            # the_numbers_match = True if randomNumber == number else False <--- or you can write it Ternary like this?
    
    # Does my_randoms contain number? Change the boolean.
    if the_numbers_match == True:
        print(f'{number} is in the random list')
    else: 
        print(f'{number} is NOT in the random list')

    