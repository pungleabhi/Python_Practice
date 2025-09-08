#Simple compound interest calculator

principle=0
rate=0
time=0
def SI_calculator():
    principle = float(input("Enter the principle: "))
    while principle < 0:
        print("Principle can't be less than zero")
        principle = float(input("Enter the principle: "))
        
    rate = float(input("Enter the interest rate: "))
    while rate < 0:
        print("Rate can't be less than zero")
        rate = float(input("Enter the interest rate: "))
    
    time = float(input("Enter the time: "))
    while time < 0:
        print("Time can't be less than zero")
        time = float(input("Enter the time: "))
        
    si = (principle * rate * time)/100
    total = principle + si
    
    print(f"Balance after {time} year/s: Rs.{total:.2f}")
    print(f"Interest after {time} year/s: Rs.{si:.2f}")
        
def CI_calculator():
    principle = float(input("Enter the principle: "))
    while principle < 0:
        print("Principle can't be less than zero")
        principle = float(input("Enter the principle: "))
        
    rate = float(input("Enter the interest rate: "))
    while rate < 0:
        print("Rate can't be less than zero")
        rate = float(input("Enter the interest rate: "))
    
    time = float(input("Enter the time: "))
    while time < 0:
        print("Time can't be less than zero")
        time = float(input("Enter the time: "))       
    
    total = principle * pow((1 + rate/100), time)
    ci = total - principle
    print(f"Balance after {time} year/s: Rs.{total:.2f}") 
    print(f"Interest after {time} year/s: Rs.{ci:.2f}")  


while True:
    print("Interest Calculator Menu")
    print("1. SI Calculator")
    print("2. CI Calculator")
    print("3. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        SI_calculator()
    elif choice == "2":
        CI_calculator()
    elif choice == "3":
        print("Exiting!!!")
        break
    else:
        print("Invalid Choice!! Please select from 1-3")
        
        
    
# principle=0
# rate=0
# time=0

# while True:
#     principle = float(input("Enter the principle: "))
#     if principle <0:
#         print("Principle can't be less than zero")
#     else:
#         break
        
# while True:
#     rate = float(input("Enter the interest rate: "))
#     if rate <0:
#         print("Interest rate can't be less than zero")
#     else:
#         break 

# while True:
#     time = int(input("Enter the time in years: "))
#     if time <0:
#         print("Time can't be less than zero")
#     else:
#         break
  
# total = principle * pow((1 + rate/100), time)
# print(f"Balance after {time} year/s: Rs.{total:.2f}") 