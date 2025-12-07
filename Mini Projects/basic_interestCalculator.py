principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Please enter a principal amount: "))
    if principle <= 0:
        print("The principal amount must be greater than 0.")

while rate <= 0:
    rate = float(input("Please enter an interest rate (as a percentage): "))
    if rate <= 0:
        print("The interest rate must be greater than 0.")

while time <= 0:
    time = int(input("Please enter the time (in years): "))
    if time <= 0:
        print("The time must be greater than 0.")

total = principle * pow((1+ rate / 100), time)
print(f"Balance after {time} year/s is: ${total:.2f}")