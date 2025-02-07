# Unit Testing for Exact Change Calculator

## Overview
This project primarily focuses on unit testing the `exact_change` function, which takes an amount in cents and figures out the right mix of quarters, dimes, nickels, and pennies to make up that total. The main focus here is testing that logic to ensure it's reliable. 

## Unit Testing
### Running the Unit Tests
To run the unit tests, use:
```bash
python -m unittest exact_change.py
```

### Test Cases
The script contains the following test cases:
- **`testPositive`**: Ensures that a valid positive input returns the correct number of quarters, dimes, nickels, and pennies. Example:
  - Input: `41` cents
  - Expected Output: `(1 penny, 1 nickel, 1 dime, 1 quarter)`

- **`testNegative`**: Ensures that a negative input correctly returns `(0,0,0,0)` and does not process change calculation.

- **`testZero`**: Checks that an input of `0` correctly results in `(0,0,0,0)`, indicating no change is needed.

These unit tests validate that the `exact_change` function handles a variety of edge cases, ensuring robustness.

## Features
- Uses `unittest` module for automated testing.
- Covers edge cases like zero and negative values.
- Ensures accurate calculation of change.

## Usage
To execute the script (apart from testing), run the following command:
```bash
python exact_change.py
```
The program will prompt for an input value and output the required coins to make exact change.

### Example Output
```
Enter the amount in cents: 41
1 quarter
1 dime
1 nickel
1 penny
```
If the input is 0 or negative, the program will output:
```
no change
```

## Requirements
- Python 3.x
- `unittest` (included with Python standard library)

## License
This project is open-source and available under the MIT License.

## Author
Cezar Pedroso

