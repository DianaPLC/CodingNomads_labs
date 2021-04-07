'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
months = {
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December"
}

month_number = ""

while type(month_number) != "int": #it's nested... they're just not all "if" statements.
    try:
        month_number = int(input("Please enter the number corresponding to your month: "))
        if 0 < month_number < 13: #could be nested I guess...
            print(months[month_number])
            break
        else:
            print("Please enter a number between 1 and 12.")
            continue
    except ValueError:
        print("Please enter a whole number.")