# Write a Python program that prints the numbers from 1 to 100.
# If a number is a multiple of three, print "Fizz" instead of the number.
# If the number is a multiple of five, print "Buzz" instead of the number.
# For numbers which are multiples of both three and five, print "FizzBuzz" instead of the number.


# If a number is a multiple of 7, print "Bang" instead of the number. 
# For numbers which are multiples of seven and three / five, append Bang to what you'd have printed anyway. (E.g. 3 * 7 = 21: "FizzBang").


# for fizzbuzz in range(101): 
#     if  fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0 and fizzbuzz % 7 and fizzbuzz & 11 == 0: 
#         print('Bong')
#         continue
#     elif fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#         print('FizzBuzz')
#         continue
#     elif fizzbuzz % 3 and fizzbuzz % 7 == 0:
#         print('FizzBang')
#         continue
#     elif fizzbuzz % 5 and fizzbuzz % 7 == 0:
#         print('BuzzBang')
#         continue
#     elif fizzbuzz % 13 == 0:
#         print('Fezz')
#         continue
#     elif fizzbuzz % 11 == 0:
#         print('Bong')
#         continue
#     elif fizzbuzz % 3 == 0:
#         print('Fizz')
#         continue
#     elif fizzbuzz % 5 == 0:
#         print('Buzz')
#         continue
#     elif fizzbuzz % 7 == 0:
#         print('Bang')
#         continue
#     else:
#         print(fizzbuzz, 'Try again')


# Creating a range 0 to 100
for i in range(1,101) :
    # initialize an empty string to concatenate values together 
    string = ""
    if i % 3==0 : string+="Fizz"
    if i % 5==0 : string+="Buzz"
    if i % 7==0 : string+="Bang"
    if string == "" : print(i)
    else : print(string)