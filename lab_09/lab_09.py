# zadanie1
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.points = [] #do zadania5

# zadanie2
    def __str__(self):
        return f"Point({self.x}, {self.y})"

#zadanie3
    def __mul__(self, factor):
            return Point(self.x * factor, self.y * factor)
    
#zadanie4
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

#zadanie 5
class Polygon:
    def __init__(self):
        self.points = []
        
    def add_point(self, point):
        if isinstance(point, Point):
            self.points.append(point)
        else:
            raise ValueError("Argument musi być instancja klasy Point")
    
    #zadanie6
    def __str__(self):
        points_str = ", ".join([str(point) for point in self.points])
        return f"Polygon[{points_str}]"
    
    #zadanie7
    def __getitem__(self, item):
        if isinstance(item, int):
            return self.points[item]
        elif isinstance(item, slice):
            return PolygonSlice(self.points[item])
        else:
            raise TypeError("error")
    
# zadanie3
p1 = Point(2, 3)
p2 = p1 * 2
print(p2)  # wynik: Point(4, 6)

# zadanie4
p1 = Point(2, 3)
p2 = Point(2, 3)
p3 = Point(4, 5)
print(p1 == p2)  # wynik: True
print(p1 == p3)  # wynik: False


#zadanie5

p1 = Point(0, 0)
p2 = Point(2, 4)
p3 = Point(5, 1)

polygon = Polygon()
polygon.add_point(p1)
polygon.add_point(p2)
polygon.add_point(p3)

#zadanie 6
p1 = Point(0, 0)
p2 = Point(2, 4)
p3 = Point(5, 1)

polygon = Polygon()
polygon.add_point(p1)
polygon.add_point(p2)
polygon.add_point(p3)

print(polygon)  # wyświetli "Polygon[Point(0, 0), Point(2, 4), Point(5, 1)]"

#zadanie 7

class PolygonSlice:
    def __init__(self, points):
        self.points = points
        
    def __str__(self):
        points_str = ", ".join([str(point) for point in self.points])
        return f"[{points_str}]"
        
    def __getitem__(self, item):
        return self.points[item]
    
p1 = Point(0, 0)
p2 = Point(2, 4)
p3 = Point(5, 1)
p4 = Point(7, 2)

polygon = Polygon()
polygon.add_point(p1)
polygon.add_point(p2)
polygon.add_point(p3)
polygon.add_point(p4)

# zwrócenie pojedynczego punktu
print(polygon[2])  # wyświetli "Point(5, 1)"

# zwrócenie wycinka punktów
slice_ = polygon[1:5]
print(slice_)  # wyświetli "[Point(2, 4), Point(5, 1)]"

# zwrócenie pojedynczego punktu z wycinka
print(slice_[1])  # wyświetli "Point(5, 1)"