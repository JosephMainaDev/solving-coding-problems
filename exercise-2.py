'''
Solution to the second exercise.

args:
    points: list of points on a Cartesian plane in the form (x, y)
returns:
   True if the points lie on a straight line, False otherwise

Example:
>>> checkStraightLine([(1,2), (2,3), (3,4), (4,5)])
>>> True

>>> checkStraightLine([(1,2), (2,3), (3,4), (4,8)])
>>> False
'''

def checkStraightLine(points):
    # Grab the first 2 points on the line
    x1, y1 = points[0]
    x2, y2 = points[1]
    # And iterate from the 3rd point to the end of the line
    for point in points[2:]:
        # Get a 3rd point
        x3, y3 = point
        # Compute the area formed by the three points
        area = 0.5*(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
        # If area is non-zero, the points are not on a straight line
        if(area != 0):
            return False
    
    # The points are on a straight line
    return True

# Test the function

def testCheckStraightLine():
    lines = [[(1,2), (2,3), (3,4), (4,5)], [(1,2), (2,3), (3,4), (4,8)]]
    for line in lines:
        print(line, "is straight:", checkStraightLine(line))
    return

testCheckStraightLine()
