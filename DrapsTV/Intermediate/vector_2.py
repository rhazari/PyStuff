import math

class Vector2D:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __add__(self,other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __iadd__(self,other):
        self.x += other.x
        self.y += other.y
        return self
    
    def __sub__(self,other):
        return Vector2D(self.x - other.x, self.y - other.y)
        
    def __isub__(self,other):
        self.x -= other.x
        self.y -= other.y
        return self
        
    def __mul__(self,other):
        return Vector2D(self.x * other.x, self.y * other.y)
        
    def __imul__(self,other):
        self.x *= other.x
        self.y *= other.y
        return self
        
    def __div__(self,other):
        return Vector2D(self.x/float(other.x), self.y/float(other.y))
        
    def __idiv__(self,other):
        self.x /= other.x
        self.y /= other.y
        return self
        
    def getAngle(self):
        return math.degrees(math.atan2(self.y, self.x))
        
    def __str__(self):
        return "X: "+str(self.x)+" Y: "+str(self.y)
        
def Main():
    vec = Vector2D(5,6)
    vec2 = Vector2D(3,2)
    
    print vec
    print vec2
    
    tempmethod = vec.getAngle
    
    vec = vec+vec2
    print vec
    
    vec *= Vector2D(2,2)
    print vec
    
    print vec.getAngle()
    
    print tempmethod()
    
if __name__ == '__main__':
    Main()
    
    
    