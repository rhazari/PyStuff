
class Vector2D:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
def Main():
    my_vec = Vector2D(5,6)
    print "X: "+str(my_vec.x)+" Y: "+str(my_vec.y)
    
if __name__ == '__main__':
    Main()

