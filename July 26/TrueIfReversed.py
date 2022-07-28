#Return True if a String is reversed..................

x = ['a','b','c','d','e']

def reversed(x):
    inverseX = ['d','c','b','a']
    if inverseX == x[::-1]:
        return True
if reversed(x):
    print('True')
else:
    print('False')
