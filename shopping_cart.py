#Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit: )")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: Rs."))
        foods.append(food)
        prices.append(price)

print("YOUR CART")

for i in range(len(foods)):
    print(f"{foods[i]:15} Rs.{prices[i]:.2f}") # here we used :15 to give 15 character spaces to align food items and prices
    #print(f"{foods[i]}  Rs.{prices[i]}")
    total += prices[i]

print("---------------")
print(f"Your total is: Rs.{total}")