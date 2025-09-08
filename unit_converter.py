#unit converter

def weight_converter():
    print("Weight Converter Menu")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    
    choice = input("Enter your choice(1-2): ")
    
    if choice == "1":
        weight = float(input("Enter your weight in Kilograms: "))
        print(f"{weight} kgs = {weight * 2.205} lbs")
    elif choice == "2":
        weight = float(input("Enter your weight in Pounds: "))
        print(f"{weight} lbs = {round(weight / 2.205)} kgs")
    else:
        print("Invalid Choice!!!")

def length_converter():
    print("Length Converter Menu")
    print("1. Meters to Feets")
    print("2. Feets to Meters")
    
    choice = input("Enter your choice(1-2): ")
    
    if choice == "1":
        length = float(input("Enter Length in meters: "))
        print(f"{length} m = {round(length * 3.281, 2)} fts")
    elif choice == "2":
        length = float(input("Enter length in Feets: "))
        print(f"{length} fts = {round(length / 3.281, 2)} m")
    else:
        print("Invalid Choice!!!")

def temp_converter():
    print("Temperature Converter Menu")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Enter your choice(1-2): ")
    
    if choice == "1":
        temp = float(input("Enter temperature in celcious: "))
        print(f"{temp} c = {round((temp * 9/5) + 32, 2)} f")
    elif choice == "2":
        temp = float(input("Enter temperature in fahrenheit: "))
        print(f"{temp} f = {round((temp - 32) * 5/9, 2)} c")
    else:
        print("Invalid Choice!!!")

def time_converter():
    print("Time Converter Menu")
    print("1. Hours to Minutes")
    print("2. Minutes to Houre")
    print("3. Minutes to Seconds")
    print("4. Seconds to Minutes")
    
    choice = input("Enter your choice(1-4): ")
    
    if choice == "1":
        time = float(input("Enter time in Hours: "))
        print(f"{time} hrs = {time * 60} min")
    elif choice == "2":
        time = float(input("Enter time in Minutes: "))
        print(f"{time} min = {time / 60} hrs")
    elif choice == "3":
        time = float(input("Enter time in Minutes: "))
        print(f"{time} min = {time * 60} sec")
    elif choice == "4":
        time = float(input("Enter time in Seconds: "))
        print(f"{time} sec = {time / 60} min")
    else:
        print("Invalid Choice!!!")

def speed_converter():
    print("Speed Converter Menu")
    print("1. Km/h to m/s")
    print("2. m/s to Km/h")
    print("3. Km/h → Miles/h")
    print("4. Miles/h → Km/h")
    
    choice = input("Enter your choice(1-4): ")
    
    if choice == "1":
        speed = float(input("Enter Speed in Km/h: "))
        print(f"{speed} Km/h = {round(speed / 3.6, 2)} m/s")
    elif choice == "2":
        speed = float(input("Enter Speed in m/s: "))
        print(f"{speed} m/s = {round(speed * 3.6, 2)} Km/h")
    elif choice == "3":
        speed = float(input("Enter Speed in Km/h: "))
        print(f"{speed} Km/h = {round(speed * 0.621, 2)} mph")
    elif choice == "4":
        speed = float(input("Enter Speed in mph: "))
        print(f"{speed} mph = {round(speed / 0.621, 2)} Km/h")
    else:
        print("Invalid Choice!!!")

def area_converter():
    print("Area Converter Menu")
    print("1. Square meters to Square feet")
    print("2. Square feet to Square meters")
    
    choice = input("Enter your choice (1-2): ")
    
    if choice == "1":
        area = float(input("Enter area in sqm: "))
        print(f"{area} sqm = {round(area * 10.764, 2)} sqft")
    elif choice == "2":
        area = float(input("Enter area in sqft: "))
        print(f"{area} sqft = {round(area / 10.764, 2)} sqm")
    else:
        print("Invalid Choice!!!")
        
def volume_converter():
    print("Volume Converter Menu")
    print("1. Liters to Gallons")
    print("2. Gallons to Liters")
    print("3. Milliliters to Ounces")
    print("4. Ounces to Milliliters")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        vol = float(input("Enter volume in Liters: "))
        print(f"{vol} liters = {round(vol * 0.264, 2)} gallons")
    elif choice == "2":
        vol = float(input("Enter volume in gallons: "))
        print(f"{vol} gallons = {round(vol / 0.264, 2)} liters")
    elif choice == "3":
        vol = float(input("Enter volume in milliliters: "))
        print(f"{vol} ml = {round(vol / 29.574, 2)} ounches")
    elif choice == "4":
        vol = float(input("Enter volume in ounches: "))
        print(f"{vol} ounches = {round(vol * 29.574, 2)} ml")
    else:
        print("Invalid Choice!!!")  
    
while True:
    print("\n Unit converter menu")
    print("1. Weight converter")
    print("2. Length converter")
    print("3. Temperature converter")
    print("4. Time Converter")
    print("5. Speed Converter")
    print("6. Area Converter")
    print("7. Volume Converter")
    print("8. Quit")
    
    choice = input("Enter your choice (1-4): ")
       
    if choice == "1":
        weight_converter()
    elif choice == "2":
        length_converter()
    elif choice == "3":
        temp_converter()
    elif choice == "4":
        time_converter()
    elif choice == "5":
        speed_converter()
    elif choice == "6":
        area_converter()
    elif choice == "7":
        volume_converter()
    elif choice == "8":
        print("Exiting... Goodbye!!!")
        break
    else:
        print("Invalid choice! Please enter 1-4.")