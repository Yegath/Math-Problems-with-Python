"""
The population of the city of X is 350000, the population of the city of Y is 980000. Due to births and migrations, 
the population of the city of X increases by 5.8% per year and the population of the city of Y by 1.9% per year. 
Accordingly, "How many years later does the population of city X exceed the population of city Y?" write a Python 
program that finds the answer to the question.
"""

population_x = 350000
population_y = 980000
year = 0

while population_x <= population_y:
    population_x += population_x*0.058
    population_y += population_y*0.019
    year += 1

print(str(year), "years later the population of city X exceed the population of city Y")
print("The population of X city is", str(int(population_x)))
print("The population of Y city is", str(int(population_y)))
