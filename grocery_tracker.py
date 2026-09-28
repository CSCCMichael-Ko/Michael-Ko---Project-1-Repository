"""
Name: Michael Ko
Project Name: grocery_tracker.py
Class: CSCI-1511-W03L (Python Programming)
Professor: Travis Burke
Date: 09/27/2026
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
    """Giving every category an empty list to add a new item to it later"""
    cart[categories[i]] = []
    i += 1

print(f"Hi {shopper_name}, your budget is ${budget:.2f}\n")

index = 0
while index < len(categories):
    """Outputting each category one at a time"""
    category = categories[index]
    print(f"--- {category} ---")

    shopping = True
    while shopping:
        """
        Goes through categories one at a time and allows one to add as many items to each category.
        Keeps asking until the user says "no" for this category
        """
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
    """Goes through each category within the dictionary; dictionary keys"""
    category = categories[category_index]
    items = sorted(cart[category]) 

    if items:
        """Only printing categories that actually have items"""
        print(f"\n{category}:")
        item_index = 0
        while item_index < len(items):
            """
            Prints item and adds its price to total_spent
            Splits item into its name and price
            """
            name, price = items[item_index]
            print(f"  {name}: ${price:.2f}")
            total_spent += price
            item_index += 1
    category_index += 1

"""Printing out results of hard budget incorporated and amount spent"""
remaining = budget - total_spent
if remaining < 0:
    print(f"\nOver budget by ${abs(remaining):.2f}!")
else:
    print(f"\nNice job — ${remaining:.2f} left in budget.")

print(f"Items purchased: {item_count}")