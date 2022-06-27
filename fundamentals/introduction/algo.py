# Write a function that given an amount of cents returns the fewest number of quarters, dimes, nickels, and pennies required to equal that amount.
#         coinCalculator(99) should return {"Quarters":3,"Dimes":2,"Nickels":0,"Pennies":4}
#     Bonus:
#         Account for Dollar increments as well (Ones/Fives/Tens/Twenties/Fifties/Hundreds)
#     Double Bonus:
#         Account for the elusive 2 dollar bills as well.

# def coin_change():

def coin(cents):
    change = {
        'Quaters': 0,
        'Dimes': 10,
        'Nickels': 5 ,
        'Pennies' : 1
        }
    while cents > 0:
        if cents>= 25:
            change["Quaters"] += 1
            cents -=25
            while cents > 25:

            elif cents>= 10:
                change["Dime"] += 1
                cents -=10
                while cents > 10:

            elif cents>= 25:
                change["Nickels"] += 1
                cents -=5
                while cents > 5:

            elif cents>= 1:
                change["Pennies"] += 1
                cents -=1