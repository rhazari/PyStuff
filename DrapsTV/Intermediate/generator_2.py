
def Main(data):
    
    rev = (data[i] for i in range(len(data)-1,-1,-1))
    for char in rev:
        print char

if __name__ == '__main__':
    Main("Raihan Hazarika")
    

