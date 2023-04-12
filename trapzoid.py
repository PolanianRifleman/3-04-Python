import math

while True:

    a = input("What is the length of side a? ")

    try:
        a = float(a)
    except ValueError:
        print("INVALID INPUT. ENTER NUMBER")
        continue

    b = input("What is the lenght of side b? ")

    try:
        b = float(b)
    except ValueError:
        print("INVALID INPUT. ENTER NUMBER")
        continue
    
    h = input("What is your height ")

    try:
        h = float(h)
    except ValueError:
        print("INVALID INPUT. ENTER NUMBER")
        continue

    c = str(h*(a+b)/2)

    print("The area of your trapizoid " + c)
    break
