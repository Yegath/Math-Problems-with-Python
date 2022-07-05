"""
From the 10 numbers entered, write a Python program that contains the following:
a) The number of positive numbers,
b) Average of positive numbers,
c) The sum of squares of all numbers,
d) The largest and smallest numbers
"""

i = 1
number_of_positive_numbers = 0
sum_of_positive_numbers = 0
sum_of_square_of_number = 0

while i < 11:
    number = float(input("Enter a number: "))

    if number > 0:
        number_of_positive_numbers += 1 
        sum_of_positive_numbers += number
        average_of_positive_numbers = sum_of_positive_numbers / number_of_positive_numbers

    square_of_number = number ** 2
    sum_of_square_of_number += square_of_number

    if i == 1:
        largest_number = number
        smallest_number = number
    
    if largest_number < number:
        largest_number = number
    
    if smallest_number > number:
        smallest_number = number

    i += 1

print("The number of positive numbers is ", str(number_of_positive_numbers))
print("Average of positive numbers is ", str(average_of_positive_numbers))
print("The sum of squares of all numbers is", str(sum_of_square_of_number))
print("The largest number is ", str(largest_number), "and smallest numbers is ", str(smallest_number))
