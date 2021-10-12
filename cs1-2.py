# author : LM (AMDG) 10/12/21
start_desposit = int(input("Enter the initial amount of investment. "))
interest_rate = float(input("Enter the annual interest rate. "))
number_years = int(input("Enter the number of years the money is in the account. "))

future_value = start_desposit * (1 + (interest_rate / 12)) ** (12 / number_years)
print("The future value of the money invested is. " + str(future_value))