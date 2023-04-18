"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math
a=float(input("Enter a first number include float values: "))
b=float(input("Enter a second number include float values: "))
a=int(round(a))
b=int(round(b))

ask=str(input("\none of the numbers is the hypotenuse of a right triangle?\n yes or no: "))

if ask == "yes" and a>b:
    print(a, "is the hypotenuse of a right triangle!")
    misside=math.sqrt(math.pow(a,2)-math.pow(b,2))
    print(round(misside,1))
elif ask == "yes" and b>a:
    print(b, "is the hypotenuse of a right triangle!")
    misside=math.sqrt(math.pow(b,2)-math.pow(a,2))
    print(round(misside, 1))
elif ask == "no":
    print("There is no hypotaneuse of a right triangle!")