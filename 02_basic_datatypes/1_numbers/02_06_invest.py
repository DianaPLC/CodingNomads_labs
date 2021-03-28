'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
investment_amount = ""
while type(investment_amount) != "float":
    try:
        investment_amount = float(input("Enter your starting investment amount: "))
        break
    except ValueError:
        print("Please enter a number.")

interest_rate = ""
while type(interest_rate) != "float":
    try:
        interest_rate = float(input("Enter the percent annual interest rate (eg. for 3.5% APR, enter 3.5: "))
        break
    except ValueError:
        print("Please enter a number.")

years = ""
while type(years) != "int":
    try:
        years = int(input("Enter the number of years you will invest: "))
        break
    except ValueError:
        print("Please enter a whole number.")

current_year = 0
while current_year <= years:
    current_amount = investment_amount*((1+(interest_rate/100))**current_year)
    print("Year ",current_year," amount: $",round(current_amount,2))
    current_year += 1
