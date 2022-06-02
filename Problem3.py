"""
Find the average of the given undetermined number of integers by keyboard. Write a Python program that prints "The average is negative!" on the screen 
if the average is negative, and "The average is equal to zero!"on the screen if the average is equal to zero, and "The average is positive!" on the screen 
if the average is positive.
"""
i = 1
s = 0

while True:
    n = int(input("Enter a number: "))
    s += n
    a = input("Is there another number? (Y/N): ")
    if a == "N":
        break
    elif a == "Y":
        i += 1
    else:
        print("Attention! Enter 'Y' for Yes, 'N' for No.")
        a = input("Is there another number? (Y/N): ")

if i != 0:
    av = s / i
    print("Average of the given undetermined number of integers is "+ str(av)+ ".")
    if av < 0:
        print("The average is negative!")
    elif av == 0:
        print("The average is equal to zero!")
    else:
        print("The average is positive!")
else:
    print("There is no given undetermined number of integers.")
