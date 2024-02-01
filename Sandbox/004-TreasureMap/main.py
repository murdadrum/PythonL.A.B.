# https://www.w3schools.com/python/ref_list_index.asp

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?")

letter = position[0].lower()
abc = ["a", "b", "c"]

# Check if letter is in abc
if letter not in abc:
    letter = "c"   # set letter to 'c' if it's not in abc

letter_index = abc.index(letter)
number_index = int(position[1]) - 1

# Check if number out of range
if number_index > 2:
    number_index = 2
if number_index < 1:
    number_index = 0

map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")
