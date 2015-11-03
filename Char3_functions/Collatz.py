__author__ = 'agorgoma'


def collatz(number):
    if number % 2 == 0:
        even = number // 2
        print(even)
        return even
    else:
        odd = 3 * number + 1
        print(odd)
        return odd

print('Enter number:')
try:
    number = collatz(int(input()))
except:
    print('Number is incorrect')

while number != 1:
    #collatz(number)
    number = collatz(number)

#collatz(3)
#s = collatz(3)