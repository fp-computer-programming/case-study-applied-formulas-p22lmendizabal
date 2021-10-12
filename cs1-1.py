# Author: LM (AMDG) 10/12/21
first_xcoordinate = int(input("Enter the first X coordinate. "))
second_xcoordinate = int(input("Enter the secomd X coordinate. "))
first_ycoordinate = int(input("Enter the first Y coordinate. "))
second_ycoordinate = int(input("Enter the second Y coordinate. "))

distance = ((second_xcoordinate - second_ycoordinate)**2 + (first_xcoordinate - first_ycoordinate)**2) ** (1/2)

print("The distance is " + str(distance))