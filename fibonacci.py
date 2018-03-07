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
