
from string import Template

class MyTemplate(Template):
    delimiter = '#'

def Main():
    cart = []
    cart.append(dict(item="Coke", price=8, qty=2))
    cart.append(dict(item="Cake", price=4, qty=1))
    cart.append(dict(item="Fish", price=20, qty=4))
    
    t = MyTemplate("#item x #qty = #price")
    total = 0
    print "Cart:"
    for data in cart:
        print t.substitute(data)
        total += data["price"]
        
    print "Total: "+str(total)
    
if __name__ == '__main__':
    Main()

