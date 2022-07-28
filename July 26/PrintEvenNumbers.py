#Get Even Number from a List.......

List = [1, 2, 4, 0, -3, -4, 'a', 'b', 'c']
evenNumbers = [x for x in List if type(x) == int and x % 2 == 0 and x > 1]
print(evenNumbers)
