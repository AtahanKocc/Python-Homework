"""
Author: Atahan Koc
Homework 1 - Question 3
Description Part: In this question, I have written a Python function called “find_fibonacci” that accepts a list as an input and,
We were asked to find and return items that meet the Fibonacci property. First, I created a list to store lists that follow the fibonacci property.
Then I tested whether the elements meet the fibonacci property. If the property fits, it is added to the output list. In the def main() section, a list with numbers separated by spaces is being entered.
Finally, I called the find fibonacci function with the input_list parameter and printed output_list. I have successfully achieved the output.
"""
def find_fibonacci(in_list):
    #list to store lists following fibonacci property
    out_list=[]
    for i in range(2,len(in_list)):
        #checking if elements follows fibonacci property
        if in_list[i]== in_list[i-1]+in_list[i-2]:
              out_list.append([in_list[i-2],in_list[i-1],in_list[i]])
    return out_list

def main():
    #taking a list of numbers separated by spaces as input
    input_list=input().split(" ")
    # converting all element to integer
    input_list = [int(i) for i in input_list]
    print(find_fibonacci(input_list))

main()