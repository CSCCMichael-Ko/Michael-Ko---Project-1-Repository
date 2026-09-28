"""
Name: Michael Ko
Project Name: grocery.tracker.py
Class: CSCI-1511-W03L (Python Programming)
Professor: Travis Burke
Date: 09/25/2026
Purpose: Tracking groceries by category against a budget. Tried to incorporate elements/topics within Chapters 1-7 of the Python Crash Course (Third Edition) Textbook.
"""

shopper_name = ""             
budget = 0.0                  
item_count = 0                

categories = []

cart = {}

index = 0
while index < len(categories):
    category = categories[index]

    shopping = True
    while shopping:
        response = input("Add an item? (yes/no): ").lower()

        if response == "yes":

        elif response == "no":
            shopping = False
        else:

    index += 1

total_spent = 0

remaining = budget - total_spent