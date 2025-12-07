menu = {
    "Hotdog": 3.50,
    "Burger": 5.99,
    "Fries": 2.45,
    "Soda": 1.75,
    "Popcorn": 4.99,
    "Candy": 2.25,
    "Ice Cream": 3.00,
    "Nachos": 4.50,
    "Pretzel": 3.75
} # Always maintain key,value pair structure

cart = []
total = 0

def display_menu():
    print("Welcome To Zootopia Theatre Stand")
    print("----MENU----")
    for key,value in menu.items():
        print(f"{key}: ${value:.2f}")
    print("------------")

display_menu()

while True:
        food = input("Enter the food item you want to order (or type 'done' to finish): ").title()
        if food == 'Done':
            break
        elif menu.get(food) is not None:
            cart.append(food)

print("----Order Summary----")
for food in cart:
    total += menu.get(food)
    print(food, end = " | ")

print()
print(f"Total Amount: ${total:.2f}")