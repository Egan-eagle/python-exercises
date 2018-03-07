# Egan Mthembu 07-03-2018
# a Python script that reads the Iris data set in and prints the four numerical values on each row.
#That is, on the screen should be printed the petal length, petal width, sepal length and sepal width, and these values should have the decimal places aligned, with a space between the columns.

with open("iris.csv") as f:
  for line in f:
    print('{:10} {:10} {:10} {:10}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))
