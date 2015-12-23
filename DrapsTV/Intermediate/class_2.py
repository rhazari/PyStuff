
class MyClass:
    names = []
    
    def add(self, name):
        self.names.append(name)
        
def Main():
    list = MyClass()
    list.add("Raihan")
    list.add("Hazarika")
    list.add("Pranami")
    
    print "Name: "+ str(list.names)
    
if __name__ == '__main__':
    Main()

