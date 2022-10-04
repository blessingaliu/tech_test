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
from re import S


for i in range(1,101) :
    # initialize an empty string to concatenate values together 
    string = ""
    if i % 11==0 : string+="Bong" 
    else :
        if i % 3==0 : string+="Fizz"
        if i % 5==0 : string+="Buzz"
        if i % 7==0 : string+="Bang"
    if string == "" : print(i)
    else : print(string)


# Alternative approach using lists 
# Creating a range 0 to 300
for i in range(1,300) :
    # initialize an empty list to add values 
    string = []
    if i % 11==0 : string.append("Bong") 
    # Only 13 goes with 11 and it goes first (inserted at index 0)
    # Every other condition has to have (not 11 within)
    # Divisible by 13 add Fezz at index 0
    if i % 13==0 : string.insert(0,"Fezz")
    # Divisible by 3, add Fizz at index 0 (Fizz always comes first)
    if i % 3==0 and not i % 11==0: string.insert(0, "Fizz")
    if i % 5==0 and not i % 11==0: string.append("Buzz")
    if i % 7==0 and not i % 11==0: string.append("Bang")
    # Divisible by 17, reverse the order
    if i % 17==0: string=string[::-1]
    # If list is empty then number 
    if string == [] : print(i)
    # join string and print it 
    else : print("".join(string))