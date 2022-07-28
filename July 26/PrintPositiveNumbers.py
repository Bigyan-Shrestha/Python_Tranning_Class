#Get Positive Number in mix List of String, positive & Negative numbers.......

List = [1, 2, 4, 0, -3, -4, 'a', 'b', 'c']
positiveNumbers = [x for x in List if type(x) == int and x >= 1]
print(positiveNumbers)
