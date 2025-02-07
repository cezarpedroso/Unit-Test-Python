import sys

def exact_change(user_total):
    money_total = user_total    # Store the total amount of money

    num_quarters = money_total // 25    # Quarters calculation
    money_total -= num_quarters * 25

    num_dimes = money_total // 10   # Dimes calculation
    money_total -= num_dimes * 10

    num_nickels = money_total // 5  # Nickels calculation
    money_total -= num_nickels * 5      

    num_pennies = money_total   # Pennies calculation
    return num_pennies, num_nickels, num_dimes, num_quarters

if __name__ == '__main__':
    input_val = int(input("Enter an amount (in cents)")) # Calling input

    if input_val <= 0:
        print("no change")
        sys.exit()  # Function from the Sys library to stop running the program if the input is equal or lower than zero

    num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)

    if num_quarters > 0:
        print(str(num_quarters), "quarter" if num_quarters == 1 else "quarters")

    if num_dimes > 0:
        print(str(num_dimes), "dime" if num_dimes == 1 else "dimes")

    if num_nickels > 0:
        print(str(num_nickels), "nickel" if num_nickels == 1 else "nickels")

    if num_pennies > 0:
        print(str(num_pennies), "penny" if num_pennies == 1 else "pennies")
