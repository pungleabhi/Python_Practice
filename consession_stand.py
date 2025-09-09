#Consession Standt Program

menu = {"pizza": 250,
        "nachos": 350,
        "popcorn": 500,
        "fries": 200,
        "chips": 100,
        "burger": 300,
        "soda": 250,
        "lemonade": 320}

cart = []
total = 0

print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}: Rs.{value:.2f}")
print("------------------------")

while True:
    food = input("Select an item ( q to quit): ").lower()
    if food == "q":
        break
    elif food in menu:
        cart.append(food)

print("------ YOUR ORDER ------")
for food in cart:
    total += menu[food]
    print(food, end=" ")

print()
print(f"Total is: Rs.{total:.2f}")