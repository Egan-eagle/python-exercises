# Egan Mthembu
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Mthembu"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

#COMMENT
Re: Week 2 task
by EGAN MTHEMBU - Saturday, 3 February 2018, 6:47 PM
 
C:\Users\egan\Desktop\fib.py\WEEK2>python test.py

My surname is Mthembu

The first letter M is number 77

The last letter u is number 117

Fibonacci number 194 is 15635695580168194910579363790217849593217

ord(c)
Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example,ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of chr().

i.e
firstno = ord(first) M = 77
lastno = ord(last)  U = 117
x = firstno + lastno  =  194
Fibonacci number 194 is 15635695580168194910579363790217849593217


WEEK1 EXERCISE

# Egan Mthembu 24.01.2018
# A program that displays Fibonacci numbers.

def fib(n):
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i
x = 19
ans = fib(x)
print("Fibonacci number", x, "is", ans)

Re: Fibonacci exercise responses
by EGAN MTHEMBU - Wednesday, 24 January 2018, 11:12 PM
 
Egan : E + N = 19, Fibonacci Number = 4181

C:\Users\ppc\Desktop\Fibonacci>python fib3.py

Fibonacci number 19 is 4181# Egan Mthembu
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Mthembu"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

#COMMENT
#Re: Week 2 task
#EGAN MTHEMBU - Saturday, 3 February 2018, 6:47 PM
#My surname is Mthembu

The first letter M is number 77

The last letter u is number 117

Fibonacci number 194 is 15635695580168194910579363790217849593217

ord(c)
Given a string repord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of chr().

i.e
firstno = ord(first) M = 77
lastno = ord(last)  U = 117
x = firstno + lastno  =  194
Fibonacci number 194 is 15635695580168194910579363790217849593217


##WEEK1 EXERCISE

# Egan Mthembu 24.01.2018
# A program that displays Fibonacci numbers.

def fib(n):
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i
x = 19
ans = fib(x)
print("Fibonacci number", x, "is", ans)

Re: Fibonacci exercise responses
by EGAN MTHEMBU - Wednesday, 24 January 2018, 11:12 PM
 
Egan : E + N = 19, Fibonacci Number = 4181

Fibonacci number 19 is 4181
