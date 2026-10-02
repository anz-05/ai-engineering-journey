rawstr = input("Enter a number: ")
try:
    num = float(rawstr)
    if num < 0:
        print("Negative")
    elif num == 0:
        print("Zero")
    elif num < 100:
        if num < 10:
            print("very small")
        else:      
            print("Small")
    else:
        print("Large")    
except:
    print("Not a number")