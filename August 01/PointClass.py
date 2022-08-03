
import math

class Point:

    global x1;
    global y1;
    x1 = 0
    y1 = 0

    def __init__(self, x2, y2):
        self.x2 = x2
        self.y2 = y2

    def distance(self):
        res = math.sqrt((self.x2 - x1)^2 + (self.y2 - y1)^2)
        print('The Distance between points p1 & p2 is '+str(res)+' units.')
        point = ['x','y']
        data = [self.x2, self.y2]
        list1 = zip(point, data)
        list2 = list(list1)
        x,y = zip(*list2)
        print('The Coordinates of the point objects is '+str(y))
    
#Passing Values to the variables inside method of the Class.......  
value = Point(2,3)

#Calling the method/function........
value.distance()

