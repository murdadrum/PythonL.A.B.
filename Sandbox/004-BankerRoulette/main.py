import random

names_string = 'Angela, Ben, Jenny, Michael, Chloe'
names = names_string.split(", ")
random_integer = random.randint(0, len(names) - 1)
print(names[random_integer], "is going to buy the meal today!")
