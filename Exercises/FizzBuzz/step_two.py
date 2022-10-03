# Write a Python program that prints the numbers from 1 to 100.
# If a number is a multiple of three, print "Fizz" instead of the number.
# If the number is a multiple of five, print "Buzz" instead of the number.
# For numbers which are multiples of both three and five, print "FizzBuzz" instead of the number.


# If a number is a multiple of 7, print "Bang" instead of the number. 
# For numbers which are multiples of seven and three / five, append Bang to what you'd have printed anyway. (E.g. 3 * 7 = 21: "FizzBang").


for fizzbuzz in range(101): 
    if  fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0 and fizzbuzz % 7 and fizzbuzz & 11 == 0: 
        print('Bong')
        continue
    elif fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print('FizzBuzz')
        continue
    elif fizzbuzz % 3 and fizzbuzz % 7 == 0:
        print('FizzBang')
        continue
    elif fizzbuzz % 5 and fizzbuzz % 7 == 0:
        print('BuzzBang')
        continue
    elif fizzbuzz % 11 == 0:
        print('Bong')
        continue
    elif fizzbuzz % 3 == 0:
        print('Fizz')
        continue
    elif fizzbuzz % 5 == 0:
        print('Buzz')
        continue
    elif fizzbuzz % 7 == 0:
        print('Bang')
        continue
    else:
        print(fizzbuzz, 'Try again')