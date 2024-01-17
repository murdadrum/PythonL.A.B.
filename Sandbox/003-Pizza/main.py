SMALL_PIZZA_PRICE = 15
MEDIUM_PIZZA_PRICE = 20
LARGE_PIZZA_PRICE = 25
PEPPERONI_SMALL_PIZZA_PRICE = 2
PEPPERONI_MED_LRG_PIZZA_PRICE = 3
EXTRA_CHEESE_PRICE = 1
BILL = 0

print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    BILL += SMALL_PIZZA_PRICE
    if add_pepperoni == "Y":
        BILL += PEPPERONI_SMALL_PIZZA_PRICE
elif size == "M":
    BILL += MEDIUM_PIZZA_PRICE
    if add_pepperoni == "Y":
        BILL += PEPPERONI_MED_LRG_PIZZA_PRICE
elif size == "L":
    BILL += LARGE_PIZZA_PRICE
    if add_pepperoni == "Y":
        BILL += PEPPERONI_MED_LRG_PIZZA_PRICE
if extra_cheese == "Y":
    BILL += EXTRA_CHEESE_PRICE
print(f"Your final bill is: ${BILL}.")
