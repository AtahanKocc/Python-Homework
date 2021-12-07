"""
Author: Atahan Koc
Description Part: The logic of this question is to find the difference between consecutive numbers, storing them in an array.
Then, the difference sequence was looped and two consecutive differences were compared.If they are the same, the entered list number is stored in that directory and in the next directory.

"""

def find_pattern(list_numbers):
    differenceArray = []
    print("Input List")
    print(list_numbers)
    index = 0
    new_list = []
    for i in range(1, len(list_numbers)):
        differenceArray.append(list_numbers[i] - list_numbers[i-1]) # storing difference between two numbers

    while index < len(differenceArray)-1:
        # checking if consecutive difference are same
        if differenceArray[index+1] == differenceArray[index]:
            new_list.append(list_numbers[index])
            while index < len(differenceArray)-1 and differenceArray[index] == differenceArray[index+1]:
                new_list.append(list_numbers[index+1]) # storing the next element
                index+=1
            new_list.append(list_numbers[index+1])
        else:
            index+=1
    print("Output List")
    print(new_list)

#result part
input_numbers = input("Enter a list of numbers separated by a space:")
list_n = input_numbers.split() # to take inputted numbers in string format
temp_map = map(int, list_n) # to convert string list into integer list but stored as map
list_numbers = list(temp_map)  # to convert map into list

find_pattern(list_numbers)