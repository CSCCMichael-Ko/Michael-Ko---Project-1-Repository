"""
Name: Michael Ko
Project Name: grocery.tracker.py
Class: CSCI-1511-W03L (Python Programming)
Professor: Travis Burke
Date: 09/25/2026
Purpose: Tracking groceries by category and comparing whats bought against a budget. Tried to incorporate elements/topics within Chapters 1-7 of the Python Crash Course (Third Edition) Textbook.
Starter Code: None, did search up how to incorporate rounding float to two decimal points. 
"""

shopper_name = "Michael Ko"
budget = 150.00               
item_count = 0              

categories = ["Produce", "Dairy", "Pantry", "Other/Miscellaneous"]

cart = {}

i = 0
while i < len(categories):
    cart[categories[i]] = []
    i += 1

print(f"Hi {shopper_name}, your budget is ${budget:.2f}\n")

"""While loop over the list"""
index = 0
while index < len(categories):
    category = categories[index]
    print(f"--- {category} ---")

    shopping = True
    while shopping:
        """Goes through categories one at a time and allows one to add as many items to each category"""
        response = input(f"Add an item to {category}? (yes/no): ").lower()
        
        if response == "yes":
            name = input("  Item name: ")
            price = float(input("  Price: "))
            cart[category].append((name, price)) 
            item_count += 1
        elif response == "no":
            shopping = False
        else:
            print("  Please answer yes or no.")

    index += 1

total_spent = 0
print("\n=== Receipt ===")
category_index = 0
while category_index < len(categories):
    """Nested while loop, outer loop picks category and uses it as key from dictionary"""
    category = categories[category_index]
    items = sorted(cart[category])
    if items:
        print(f"\n{category}:")
        item_index = 0
        while item_index < len(items):
            """"""
            name, price = items[item_index]
            print(f"  {name}: ${price:.2f}")
            total_spent += price
            item_index += 1
    category_index += 1

"""Printing out results of hard budget incorporated and amount spent"""
remaining = budget - total_spent
if remaining < 0:
    print(f"\nOver budget by ${abs(remaining):.2f}!")
elif remaining < 10:
    print(f"\nCutting it close — ${remaining:.2f} left.")
else:
    print(f"\nNice job — ${remaining:.2f} left in budget.")

print(f"Items purchased: {item_count}")