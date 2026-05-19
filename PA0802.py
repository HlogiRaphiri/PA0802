# PA0802 - n = n + 1 means n takes the new value of whatever n + 1 is

#1.2 Provide code for a python3 function that takes a list of numbers as an argument, then returns the lowest and second lowest numbers in the list as a tuple (lowest, low).'''

def two_lowest(numbers):
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers.")
    
    lowest = float('inf')
    low = float('inf')

    for n in numbers:
        if n < lowest:
            low = lowest
            lowest = n
        elif n < low:
            low = n

    return (lowest, low)
#Example
print(two_lowest([4, 1, 7, 2, 9]))
print(two_lowest([7, 3, 9, 1, 5]))  