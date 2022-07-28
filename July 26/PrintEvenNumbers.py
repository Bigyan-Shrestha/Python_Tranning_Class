#Get Even Number from a List.......

List = [1, 2, 4, 0, -3, -4, 'a', 'b', 'c']

#Getting Positive Even Numbers only.......
evenNumbers = [x for x in List if type(x) == int and x % 2 == 0 and x > 1]
print(List)
print('The Even Numbers in List = '+ str(evenNumbers))
