# Welcome Statement
print("Welcome to Akilesh Roller Coaster!")

# Bill variable
bill = 0

# Checking height and getting age for allotting their price.
height = int(input("Type your height in cm: "))
if height > 120:
    print("You can go and enjoy the ride.")
    age = int(input("Type your age: "))
    if age < 10:
        bill += 300
        print("You need to pay ₹300.")
    elif age < 14:
        bill += 400
        print("You need to pay ₹400.")
    elif age < 18:
        bill += 450
        print("You need to pay ₹450")
    elif age >= 45 and age <= 55:
        bill = 0
    else:
        bill += 500
        print("You need to pay 500")

    want_photo = input("Do you want a photo taken? Y for yes and N for no.:  ")
    if want_photo == "Y":
        bill += 10

    print(f"Your final bill amount is ₹{bill}.")

else:
    print("Sorry, you need to grow taller to get a ride.")

