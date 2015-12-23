
class MyClass:
    number = 0 ;
    name = "no_name"
    
def Main():
    me = MyClass()
    me.number = 84450
    me.name = "Raihan"
    
    friend = MyClass()
    friend.number = 33708392
    friend.name = "Hazarika"
    
    print "Name: "+me.name+" Number "+str(me.number)
    print "Name: "+friend.name+" Number "+str(friend.number)
    
if __name__ == '__main__':
    Main()
