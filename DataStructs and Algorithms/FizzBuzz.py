# very popular software engineering interview question
# Write a program that prints the numbers from 1 to n and for 
# multiples of ‘3’ print “Fizz” instead of the number and for 
# the multiples of ‘5’ print “Buzz”. If the number is divisable by 
# both 3 and 5, print FizzBuzz

def fizzBuzz():
    n = 100

    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)

if __name__ == '__main__':
    fizzBuzz()