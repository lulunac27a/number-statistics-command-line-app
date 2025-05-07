from typing import Any#type annotations
import numpy as np#use NumPy library

numbers = []#array of numbers
while True:
    print("Enter a number: ")#enter number value to add to list
    number_input: str = input()#read input
    try:
        numbers.append(int(number_input))#parse input as integer and add to list
    except ValueError:
        print("Invalid input. It will now print the statistics.")
        break#if input is not a number, break out of loop and print statistics
numbers = np.array(numbers)#convert list to NumPy array
if len(numbers) == 0:#check if list is empty
    print("No numbers entered. The program will now end.")
else:
    print("Minimum: ", np.min(numbers))#minimum value
    print("First quartile: ", np.percentile(numbers, 25))#first quartile value
    print("Median: ", np.median(numbers))#median value
    print("Third quartile: ", np.percentile(numbers, 75))#third quartile value
    print("Maximum: ", np.max(numbers))#maximum value
    print("Mean: ", np.mean(numbers))#mean value
    print("Standard deviation: ", np.std(numbers))#standard deviation value
    while True:
        print("Enter quartile value: ")
        quartile_input: str = input()#read input
        try:
            quartile_value = float(quartile_input)
            if quartile_value >= 0 and quartile_value <= 1:
                print("Quartile value: ", np.percentile(numbers, quartile_value * 100))#print quartile value
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. The program will now end.")
            break#end the program