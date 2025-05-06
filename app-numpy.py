import numpy as np

numbers = np.array([])
while True:
    print("Enter a number: ")
    number_input = input()
    try:
        numbers = np.append(numbers, int(number_input))
    except ValueError:
        print("Invalid input. It will now print the statistics.")
        break
print("Minimum: ", np.min(numbers))
print("First quartile: ", np.percentile(numbers, 25))
print("Median: ", np.median(numbers))
print("Third quartile: ", np.percentile(numbers, 75))
print("Maximum: ", np.max(numbers))
print("Mean: ", np.mean(numbers))
print("Standard deviation: ", np.std(numbers))
while True:
    print("Enter quartile value: ")
    quartile_input = input()
    try:
        print("Quartile value: ", np.percentile(
            numbers, float(quartile_input) * 100))
    except ValueError:
        print("Invalid input. The program will now end.")
        break
