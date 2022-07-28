#Count the Vowel Letters in the entered String........... 

character = input('Enter a String: ')
count = sum([1 for char in character if char in 'aeiouAEIOU'])
print('Total Number Of Vowels = ' + str(count))
