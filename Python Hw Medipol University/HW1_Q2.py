"""
Author: Atahan Koc
Homework 1 - Question 2
Description Part: In this question, we were asked to use nested loops to display the pattern.
I started by typing the number of rows first, then I started the loop to print each line. Next, I wrote my loop to print spaces,
for example, print 1 space for i = 0, print 2 spaces for i = 2. Then I printed these loop numbers from 2^0 to 2^ in ascending order.
In the next loop, I printed the loop numbers in descending order. I got the desired image from us.
"""

def main():
    #number of rows
    n=8
    #loop to print each row
    for i in range(0,n):
        # loop to print spaces
        for j in range(0,n-i-1):
            print(end="  ")
        for k in range(0,i+1):  #this loop print the numbers in increasing order from 2^0 to 2^i
            print(2**k,end=" ")
        #this loop print the numbers in decreasing order from 2^(i-1) to 2^0
        for k in range(i-1,-1,-1):
            print(2**k, end=" ")
        print()
main()

