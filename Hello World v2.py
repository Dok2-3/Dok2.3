import time
from datetime import date

# Viarable List

# name
# birth_year
# m_height
# f_height
# location

#SEC 1

print("Hello")
print("")
time.sleep(2)
print("Im going to create a data file about you...")
time.sleep(2)
print("i'll assume that's ok?")
time.sleep(1.5)
print("So lets go.")
time.sleep(3)

#SEC 2

print("")
name = input("Please enter your name to begin: ")
print("")
time.sleep(0.5)
print("Hello " + name)
print("")
time.sleep(0.5)

age = int(input("How old are you? "))
current_year = date.today().year
birth_year = current_year - age
time.sleep(0.5)

m_height = int(input("What is your height in centimetres? "))
f_height = m_height / 2.54
time.sleep(0.5)

birth_place = input("Where were you born? ")
time.sleep(0.5)

location = input("Where do you live? ")
time.sleep(2)

#SEC 3

print("")
print("Thank you for cooperating")
print("This is your file")
print("")
time.sleep(2)

print("Name: " + name)
print("Age: " + str(age))
print("Birth Year: " + str(birth_year))
print("Metric Height (cm): " + str(m_height))
print("Imperial Height (in): " + str(f_height))
print("Birth Place: " + birth_place)
print("Location: " + location)
