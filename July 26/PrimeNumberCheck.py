#Check Wheather a number is prime or Not...........

a = int(input('Enter a Number:'))
if a > 1:
    for x in range(2, a):
        if (a % x) == 0:
            print(a, "is not a prime number")
            break
    else:
        print(a, "is a prime number")
else:
    print(a, "is not a prime number")
