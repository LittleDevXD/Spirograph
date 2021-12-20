import turtle
import math
import random

t = turtle.Turtle()
turtle.title("Spirograph!")

def draw(xc, yc, R, r, l, col):
    # turtle object
    t.color(*col)

    a = 0.0
    gcd_val = math.gcd(r, R)
    nRot = r // gcd_val
    step = 5
    k = r/float(R)

    # set the starting position
    t.up()
    x = R*((1-k)*math.cos(a)+l*k*math.cos((l-k)*a/k))
    y = R*((1-k)*math.sin(a)-l*k*math.sin((l-k)*a/k))
    t.setpos(xc + x, yc + y)
    t.down()

    # draw the actual spirograph
    for i in range(0, 360*nRot + 1, step):
        a = math.radians(i)
        x = R*((1-k)*math.cos(a)+l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a)-l*k*math.sin((1-k)*a/k))
        t.setpos(xc + x, yc + y)

def generate_random_param():
    # ask if the user wants a random spirograph or not
    random_or_not = input("Do you want computer to generate a random spirograph?[y/n]: ")
    # Random
    if random_or_not == "y":
        R = random.randint(100, 350)
        r = random.randint(10, 8*R//10)
        l = random.uniform(0, 0.9)
        xc = 0
        yc = 0
        col = (random.random(),
            random.random(), 
            random.random())
    # Not Random
    elif random_or_not == "n":
        R = int(input("Big circle radius: "))
        r = int(input("Small circle radius: "))
        l = float(input("Distance between big and small circle: "))
        xc = int(input("X cordinate value: "))
        yc = int(input("Y cordinate value: "))
        col = (random.random(),
               random.random(), 
               random.random())

    return (xc, yc, R, r, l, col)

try:   
    parameters = generate_random_param()
except:
    print("Invalid input!")
else:
    draw(*parameters)

# make sure the window do not close until we hit quit
turtle.mainloop()
