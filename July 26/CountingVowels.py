#Count the Vowel Letters in the entered String.......

character = input('Enter a String: ')

#Adds 1 each time vowel is found inside entered String..... 
count = sum([1 for char in character if char in 'aeiouAEIOU'])
print('Total Number Of Vowels = ' + str(count))
