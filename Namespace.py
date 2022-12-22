def Assign(i, f, s, b):
    # Write your code here
    w = i 
    x = f
    y = s
    z = b 
    print(w)
    print(x)
    print(y)
    print(z)
    print(dir())
    
if __name__ == '__main__':

    i = int(input().strip())

    f = float(input().strip())

    s = input()

    b = input().strip()
    
    Assign(i, f, s, b)
