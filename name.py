import re

while True:
    x = input("Enter your name: ")
    if x == "":
        print("Name cannot be empty.")
        continue
    elif re.search(r'\d', x):
        print("Name cannot have number.")
        continue
    else:
        print(f"Hi {x},have a great day!")
    break