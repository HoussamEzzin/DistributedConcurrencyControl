

def read(value):
    return value

def write(value):
    print('Saved ,',value)

def t1(x,amt,y):
    read(x)
    if x == None:
        print("account not found")
        return None
    x = x -amt
    if x<0:
        print("insufficient funds")
        return None
    read(y)
    if y == 0:
        print("account not found")
        return None
    y = y+amt
    write(y)
    return True