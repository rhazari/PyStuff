
import argparse

def fib(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a
    
def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("value",help="The fibonnaci number you wish to calculate.",type=int)

    args = parser.parse_args()
    result = fib(args.value)
    
    print "The "+str(args.value)+"th fib number is: "+str(result)

if __name__ == '__main__':
    Main()    

