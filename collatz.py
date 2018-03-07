# Egan Mthembu 07.02.2018
# https://en.wikipedia.org/wiki/Collatz_conjecture
# The Collatz conjecture is a conjecture in mathematics that 
# concerns a sequence defined as follows: start with any positive integer n. 
# Then each term is obtained from the previous term as follows: 
# if the previous term is even, the next term is one half the previous term. 
# Otherwise, the next term is 3 times the previous term plus 1. 
# The conjecture is that no matter what value of n, the sequence will always reach 1.


print('Please enter any number!')
number = int(input())
while number > 1 :
    if number % 2 == 0 :
       number = number //2
       print(number)
    elif number % 2 == 1:
         number = 3 * number + 1
         print(number)
    if number == 1:
       break
