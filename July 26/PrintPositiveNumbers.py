#Get Positive Number in mix List of String, positive & Negative numbers.......

List = [1, 2, 4, 0, -3, -4, 'a', 'b', 'c']

#Getting Number from list Which is greater than 1.........
positiveNumbers = [x for x in List if type(x) == int and x >= 1]
print(List)
print('Positive Numbers in List = '+str(positiveNumbers))
