import math


class Point:

    def __init__(self, x=0, y=0):
        self.coordinateX = x
        self.coordinateY = y

    def __str__(self):
        return "({}, {})".format(self.coordinateX, self.coordinateY)

    def quadrant(self):
        x = self.coordinateX
        y = self.coordinateY

        if x > 0 and y > 0:
            return "First quadrant"
        elif x < 0 and y > 0:
            return "Second quadrant"
        elif x < 0 and y < 0:
            return "Third quadrant"
        elif x > 0 and y < 0:
            return "Fourth quadrant"
        elif x != 0 and y == 0:
            return "Over X axis"
        elif x == 0 and y != 0:
            return "Over Y axis"
        else:
            return "Over origin"

    def vector(self, point):
        vectorX = point.coordinateX - self.coordinateX
        vectorY = point.coordinateY - self.coordinateY
        return {'x': vectorX, 'y': vectorY}

    def distance(self, point):
        x = pow(point.coordinateX - self.coordinateX, 2)
        y = pow(point.coordinateY - self.coordinateY, 2)
        return math.sqrt(x + y)


class Rectangle:

    def __init__(self, initial = Point(), final = Point()):
        self.intialPoint = initial
        self.finalPoint = final

    def base(self):
        return abs(self.intialPoint.vector(self.finalPoint)["x"])

    def height(self):
        return abs(self.intialPoint.vector(self.finalPoint)["y"])

    def area(self):
        return self.base() * self.height()


# Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
pointA = Point(2, 3)
pointB = Point(5, 5)
pointC = Point(-3, -1)
pointD = Point(0, 0)

print("----POINTS COORDINATES----")
print(str(pointA))
print(str(pointB))
print(str(pointC))
print(str(pointD))

# Consulta a que cuadrante pertenecen el punto A, C y D.
print("----POINTS QUADRANTS----")
print(pointA.quadrant())
print(pointC.quadrant())
print(pointD.quadrant())

# Consulta los vectores AB y BA.
print("----POINTS VECTORS----")
print(pointA.vector(pointB))
print(pointB.vector(pointA))

# Consulta la distancia entre los puntos 'A y B' y 'B y A'.
print("----POINTS DISTANCE----")
print(pointA.distance(pointB))
print(pointB.distance(pointA))

# Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
print("----POINTS DISTANCE TO ORIGIN----")

def max_distance_to_origin():
    a = pointA.distance(pointD)
    b = pointB.distance(pointD)
    c = pointC.distance(pointD)

    if (a > b and a > c):
        print("Point A is the farthest from the origin: " + str(a))
    if (b > a and b > c):
        print("Point B is the farthest from the origin: " + str(b))
    if (c > a and c > b):
        print("Point C is the farthest from the origin: " + str(c))

max_distance_to_origin()

# Crea un rectángulo utilizando los puntos A y B y consulta su base, altura y área.
print("----RECTANGLE DATA----")
rectangle = Rectangle(pointA, pointB)
print(rectangle.base())
print(rectangle.height())
print(rectangle.area())
