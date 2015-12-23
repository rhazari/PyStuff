
class Pet:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sound(self):
        raise NotImplementedError("Subclass must be implemented!")
        
class Cat(Pet):
    
    def __init__(self, name, age):
        Pet.__init__(self, name, age)
        
    def sound(self):
        return "Meow!"
        
class Dog(Pet):
    
    def __init__(self, name, age):
        Pet.__init__(self, name, age)
        
    def sound(self):
        return "Woff!"
        
def Main():
    
    tom = Pet("Tom",1)    
    jerry = Cat("Jerry",3)

    print "is Tom a Pet? "+str(isinstance(tom, Pet)) 
    print "is Tom a Cat? "+str(isinstance(tom, Cat))

    print "is Jerry a Pet? "+str(isinstance(jerry, Pet)) 
    print "is Jerry a Cat? "+str(isinstance(jerry, Cat))

    pets = [Cat("terry",2), Dog("waffle",3), Pet("Pong",3), Cat("Pren",5)]
    
    for pet in pets:
        print "Name: "+pet.name+" Age: "+str(pet.age)+" sound: "+pet.sound()
    
if __name__ == '__main__':
    Main()
    
