# The algorithm that calculates the average of 5 entered numbers.

t = 0
i = 1

while i < 6:
    try:
        s = int(input("Enter "+ str(i) + ".number: "))
    except:
        print("Attention! Please Enter a Number.")
        continue
    else:
        t += s
        i += 1
a = t / (i - 1)
print("the average of this five entered numbers is "+ str(a))
