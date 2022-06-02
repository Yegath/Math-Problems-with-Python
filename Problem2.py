# For given 5 (a,b,c,d) integer data group Y is calculated as Y=(a+b)/(c+d) by taking denominator not to be indefinite into consideration. Write a Python program to find
# a) Average of calculated negative Y values.
# b) The biggest Y value and the group a,b,c,d giving this biggest value.

i = 1
s = 0
k = 0

while i < 6:
    print("Enter "+ str(i) + ".data group.(Please be careful c+d must not equals to 0)")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    d = int(input("Enter fourth number: "))

    if (c + d) == 0:
        print("Be careful c+d must not equals to 0!")
        c = int(input("Enter third number: "))
        d = int(input("Enter fourth number: "))

    y = (a + b) / (c + d)

    if y < 0:
        k += 1
        s += y
        print(k)

    if i == 1:
        bigy = y
        biga = a
        bigb = b
        bigc = c
        bigd = d

    if bigy < y:
        bigy = y
        biga = a
        bigb = b
        bigc = c
        bigd = d

    i += 1

if k != 0:
    av = s / k
    print("Average of calculated negative Y values is "+ str(av)+ ".")
else:
    print("There are not negative Y values.")

print("Biggest Y value is "+ str(bigy)+ " and the group a,b,c,d giving this biggest value are "+ str(biga)+ " "+ str(bigb)+ " "+ str(bigc)+ " "+ str(bigd)+ ".")
