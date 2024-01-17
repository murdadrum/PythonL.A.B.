def count_characters(string, characters):
    return sum(string.count(character) for character in characters)


print("The Love Calculator is calculating your score...")
first_name = input("What is your name? ")
second_name = input("What is their name? ")

joined_names = (first_name + second_name).lower()

true_count = count_characters(joined_names, 'true')
love_count = count_characters(joined_names, 'love')

score = int(str(true_count) + str(love_count))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
