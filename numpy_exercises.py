## This py file will be used to practice some exercises using the Numpy library


## USe the code below to work with questions 1-8

import numpy as np # make sure to do your imports :)

a = np.array([4,10,12,23,-2,-1,0,0,0,-6,3,-7])


print('Exercise 1')
print('How many negative numbers are there?')
print(f'There are {len(a[a < 0])} negative numbers')


print('')
print('Exercise 2')
print('How many positive numbers are there?')
print(f'There are {len(a[a > 0])} positive numbers')

print('')
print('Exercise 3')
print('How many even positive numbers are there?')
b = a[a > 0]
print(f'There are {len(b[b % 2 == 0])} even and positive numbers')

print('')
print('Exercise 4')
print('If you were to add 3 to each data point, how many positive numbers are there?')
b = a + 3
print(f'There are {len(b[b > 0])} positive numbers if we add 3 to every number in the array')

print('')
print('Exercise 5')
print('If you squared each number, what would is the mean and standard deviation?')
b = a ** 2
print(f'The mean of the square array is {np.mean(b)} and the standard deviation would be {np.std(b)}')

print('')
print('Exercise 6')
print('Center the data')
b = a - (np.mean(a))
print(f'The new centered array data set is {b}')

print('')
print('Exercise 7')
print('Calculate the z-score for each data point')
c = b / np.std(a)
print(c)

print('')
print('Exercise 8')

# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Use python\'s built in functionality/operators to determine the following:')
print('')

print('Exercise 1') # -  Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
print(sum_of_a)
print('')

print('Exercise 2') # - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
print(min_of_a)
print('')

print('Exercise 3') # - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
print(max_of_a)
print('')

print('Exercise 4') # - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum(a) / len(a)
print(mean_of_a)
print('')

print('Exercise 5') # - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = 1
for n in a:
    product_of_a = product_of_a * n
print(product_of_a)
print('')

print('Exercise 6') #  - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [a * a for a in a]
print(squares_of_a)
print('')

print('Exercise 7') # - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = []
for x in a:
    if x % 2 == 1:
        odds_in_a.append(x)
print(odds_in_a)
print('')

print('Exercise 8') # - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = []
for x in a:
    if x % 2 == 0:
        evens_in_a.append(x)
print(evens_in_a)
print('')
## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, 
## average, sum, product, and list of squares for this list of two lists.

print('Dataset 2: 2D data manipulation with the array b below')

b = [
    [3, 4, 5],
    [6, 7, 8]
]
## First I want to convert b to a numpy array so I will use list comprehension
b = [
    [3,4,5],
    [6,7,8]
]
arrayb = np.array([np.array(i) for i in b])
print(arrayb)
print('')

print('Exercise 1') # - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

sum_of_b = np.sum(arrayb)
print(f'The sum of array b is {sum_of_b}')
print('')

print('Exercise 2') # - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])

min_of_b = np.min(arrayb)
print(f'the min af array b is {min_of_b}')
print('')

print('Exercise 3') # - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = np.max(arrayb)
print(f'The max of array b is {max_of_b}')
print('')


print('Exercise 4') # - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

mean_of_b = np.mean(arrayb)
print(f'The mean of array b is {mean_of_b}')
print('')

print('Exercise 5') # - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

product_of_b = np.product(arrayb)
print(f'The product of array b is {product_of_b}')
print('')

print('Exercise 6') # - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

squares_of_b = np.square(arrayb)
print('The Squared array of b')
print(squares_of_b)
print('')


print('Exercise 7') # - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

odds_in_b = arrayb[arrayb % 2 == 1]
print('The odds for array b')
print(odds_in_b)
print('')


print('Exercise 8') # - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

evens_in_b = arrayb[arrayb % 2 == 0]
print('The evens for array b')
print(evens_in_b)
print('')

print('Exercise 9 - print out the shape of the array b.')
print(np.shape(arrayb))
print('')

print('Exercise 10 - transpose the array b.')
print(np.transpose(arrayb))
print('')

print('Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)')
arrayc = arrayb.reshape(1,6)
print(arrayc)
print('')

print('Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)')
arrayc = arrayb.reshape(6,1)
print(arrayc)
print('')
print('Data Set 3 a three rowed matrix')
## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

arrayc = np.array([np.array(i) for i in c])
print(arrayc)
print('')

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
print('Exercise 1 - Find the min, max, sum, and product of c.')
min_of_c= np.min(arrayc)
print(f'The min value for array c is {min_of_c}')
max_of_c = np.max(arrayc)
print(f'The max value of array c is {max_of_c}')
sum_of_c = np.sum(arrayc)
print(f'The sum of array c is {sum_of_c}')
product_of_c = np.product(arrayc)
print(f'The product of array c is {product_of_c}')
print('')

print('Exercise 2 - Determine the standard deviation of c.')
stddev_c = np.std(arrayc)
print(f'The standard deviation of array c is {stddev_c}')
print('')

print('Exercise 3 - Determine the variance of c.')
variance_c = np.var(arrayc)
print(f'The variance of array c is {variance_c}')
print('')

print('Exercise 4 - Print out the shape of the array c')
shape_of_c = np.shape(arrayc)
print('The shape of array c is')
print(shape_of_c)
print('')

print('Exercise 5 - Transpose c and print out transposed result.')
print('The transposed version of array c is')
print(np.transpose(arrayc))
print('')

print('Exercise 6 - Get the dot product of the array c with c')
dot_product = np.dot(arrayc, c)
print(dot_product)
print('') 

print('Exercise 7 - sum up the result of c times c transposed. Answer should be 261')
c_times_c = arrayc * np.transpose(arrayc)
print(f'The sum of the multiplied arrays is {np.sum(c_times_c)}')
print('')

print('Exercise 8 - determine the product of c times c transposed.') 
print('Answer should be 131681894400.')
product_of_double_c = np.product(arrayc * np.transpose(arrayc))
print(f'The product of the multiplied arrays is {product_of_double_c}')
print('')


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

arrayd = np.array([np.array(i) for i in d])
print(arrayd)
print('')

print('Exercise 1 - Find the sine of all the numbers in d')
sine_of_d = np.sin(arrayd)
print(sine_of_d)
print('')

print('Exercise 2 - Find the cosine of all the numbers in d')
cosine_of_d = np.cos(arrayd)
print(cosine_of_d)
print('')

print('Exercise 3 - Find the tangent of all the numbers in d')
tangent_of_d = np.tan(arrayd)
print(tangent_of_d)
print('')

print('Exercise 4 - Find all the negative numbers in d')
negatives_in_d = arrayd[arrayd < 0]
print(negatives_in_d)
print('')

print('Exercise 5 - Find all the positive numbers in d')
positives_in_d = arrayd[arrayd > 0]
print(positives_in_d)
print('')

print('Exercise 6 - Return an array of only the unique numbers in d.')
uniques_in_d = np.unique(arrayd)
print(uniques_in_d)
print('')

print('Exercise 7 - Determine how many unique numbers there are in d.')
length_of_uniques = len(np.unique(arrayd))
print(length_of_uniques)
print('')

print('Exercise 8 - Print out the shape of d.')
print(np.shape(arrayd))
print('')

print('Exercise 9 - Transpose and then print out the shape of d.')
transposed_d = np.transpose(arrayd)
print(np.shape(transposed_d))
print('')

print('Exercise 10 - Reshape d into an array of 9 x 2')
reshaped_d = arrayd.reshape(9,2)
print(reshaped_d)