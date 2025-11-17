from math import sqrt

class Point2D:

    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    def distance_to_origine(self):
        return sqrt(self.x**2 + self.y**2)
    
    def distance_to_other(self, other) -> float :
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2 )
    
point_a = Point2D(3, 3)
point_b = Point2D(4, 5)
print(round(point_a.distance_to_other(point_b), 2))