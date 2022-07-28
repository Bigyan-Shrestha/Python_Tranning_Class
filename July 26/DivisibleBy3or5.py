#Display 'Fizz' If multiple of 3, 'Buzz' If it is of 5 or 'FizzBuzz' if it is of Both........

numbers = list(range(1,101))
for x in numbers:
    if x % 3 == 0 and x % 5 == 0:
        print(x,'= FizzBuzz')
    elif x % 3 == 0:
        print(x,'= Fizz')
    elif x % 5 == 0:
        print(x,'= Buzz')
    else:
        print(x,'= Not a Multiple of 3 or 5')
