"""
Author: Atahan Koc
Homework 1 - Question 1
Description Part: In this question, we were asked to find all the prime numbers that provide the given equation.
First, I taking an empty list. To check the conditions, I took the k-cycle and the l-cycle sorted (0,17).
Then I tried to find the numbers using the formula given later. Then I tested whether it was prime or not.
Finaly, i printed an ordered sequence of prime numbers that meets the condition.
"""
# empty list
list1=[]
# k and l loop checking for conditions
for k in range(0,17):
   for l in range(0,17):
       # find the numbers using the given formula
       num=(2**k)+(3**l)
       count=0
       #checking whether it's prime or not
       for i in range(2,int(num**0.5)+1):
          if num%i==0:
            count+=1
       if count==0:
        list1.append(num)
        # print an ordered sequence of primes that meets the condition
        list1=sorted(set(list1))

print(list1)

