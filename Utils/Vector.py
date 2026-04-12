import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = math.sqrt(x**2 + y**2)
        self.angle = math.atan2(y, x)

    @classmethod
    def from_polar(cls, distance, angle):
        x = distance * math.cos(angle)
        y = distance * math.sin(angle)
        return cls(x, y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y) + " distance: " + str(self.distance) + " angle: " + str(self.angle)

    def __bool__(self):
        return bool(self.distance)

    def rotate_by(self, angle):
        self.angle += angle
        self.x = self.distance * math.cos(angle)
        self.y = self.distance * math.sin(angle)

    def rotate_to(self, angle):
        self.angle = angle
        self.x = self.distance * math.cos(angle)
        self.y = self.distance * math.sin(angle)

    def set_distance(self, length):
        self.distance = length
        self.x += self.distance * math.cos(self.angle)
        self.y += self.distance * math.sin(self.angle)