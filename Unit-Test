import unittest
import sys

def exact_change(user_total):
    if user_total <= 0:
        return 0, 0, 0, 0  # Return 0 is equal to "no change" output

    money_total = user_total

    num_quarters = money_total // 25  # Quarters calculation
    money_total -= num_quarters * 25

    num_dimes = money_total // 10  # Dimes calculation
    money_total -= num_dimes * 10

    num_nickels = money_total // 5  # Nickels calculation
    money_total -= num_nickels * 5

    num_pennies = money_total  # Pennies calculation

    return num_pennies, num_nickels, num_dimes, num_quarters
    
    # The code above is part of the source code

class TestSum(unittest.TestCase):   # This is where the Unit Testing begins

    def testPositive(self):  # Unit Test for a positive input, in this case 41 is the input, and (1,1,1,1) is the expected result
        self.assertEqual(exact_change(41), (1, 1, 1, 1))  # 1 penny, 1 nickel, 1 dime, 1 quarter 

    def testNegative(self):  # Unit Test for a negative input, in this case -10 is the input, and (0,0,0,0) is the expected result
        self.assertEqual(exact_change(-10), (0, 0, 0, 0))  # No change for negative input

    def testZero(self):  # Unit Test for zero as the input, (0,0,0,0) is the expected result
        self.assertEqual(exact_change(0), (0, 0, 0, 0))  # No change for zero input

if __name__ == '__main__':
    unittest.main()    # Calling the Unittest function after the library was already imported
   
    if input_val <= 0:
        print("no change")
        sys.exit()    # Function from the Sys library to stop running the program if the input is equal or lower than zero


    # The code below is just part of the source code

    num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)

    if num_quarters > 0:
        print(str(num_quarters), "quarter" if num_quarters == 1 else "quarters")

    if num_dimes > 0:
        print(str(num_dimes), "dime" if num_dimes == 1 else "dimes")

    if num_nickels > 0:
        print(str(num_nickels), "nickel" if num_nickels == 1 else "nickels")

    if num_pennies > 0:
        print(str(num_pennies), "penny" if num_pennies == 1 else "pennies")
