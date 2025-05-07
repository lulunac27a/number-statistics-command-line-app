from typing import Any  # type annotations
import numpy as np  # use NumPy library

numbers: np.ndarray[Any, np.dtype[np.int_]] = np.array(
    [], dtype=int
)  # array of numbers
while True:
    print("Enter a number: ")  # enter number value to add to list
    number_input: str = input()  # read input
    try:
        numbers = np.append(
            numbers, int(number_input)
        )  # parse input as integer and add to list
    except ValueError:
        print("Invalid input. It will now print the statistics.")
        break  # if input is not a number, break out of loop and print statistics
print("Minimum: ", np.min(numbers))  # minimum value
print("First quartile: ", np.percentile(numbers, 25))  # first quartile value
print("Median: ", np.median(numbers))  # median value
print("Third quartile: ", np.percentile(numbers, 75))  # third quartile value
print("Maximum: ", np.max(numbers))  # maximum value
print("Mean: ", np.mean(numbers))  # mean value
print("Standard deviation: ", np.std(numbers))  # standard deviation value
while True:
    print("Enter quartile value: ")
    quartile_input: str = input()  # read input
    try:
        print(
            "Quartile value: ",
            np.percentile(numbers, float(quartile_input) * 100),
        )  # print quartile value
    except ValueError:
        print("Invalid input. The program will now end.")
        break  # end the program
