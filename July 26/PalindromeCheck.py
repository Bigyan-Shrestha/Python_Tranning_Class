#Check Wheather a String is Palindrome or Not..................

reversedString = 0
x = input('Enter a String: ')
reversedString = x[::-1]
if reversedString == x:
    print(x,"is a palindrome. ")
else:
    print(x,"is not a palindrome. ")

