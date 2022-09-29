# **For loop - to print numbers 1 to 100** 

for fizzbuzz in range(101): 
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print('FizzBuzz')
        continue
    elif fizzbuzz % 3 == 0:
        print('Fizz')
        continue
    elif fizzbuzz % 5 == 0:
        print('Buzz')
        continue
    else:
        print(fizzbuzz, 'Try again')


# **Take number input from user** 

num = int(input('Please enter a number from 1 to 100: '))

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return('FizzBuzz')
    elif num % 3 == 0:
        return('Fizz')
    elif num % 5 == 0:
        return('Buzz')
    else:
        return(num, "Try another number")

print(fizzbuzz(num))