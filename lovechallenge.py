import turtle
import numpy as np
import random
import time

def Desenhando():
    t = turtle.Turtle()
    s = turtle.Screen()

    t.speed(0)

    t.penup()
    t.goto(0, -200)
    t.pendown()

    for f in np.linspace(0, 2 * np.pi, 1000):
        x = 16 * np.sin(f) ** 3
        y = 13 * np.cos(f) - 5 * np.cos(2 * f) - 2 * np.cos(3 * f) - np.cos(4 * f)
        t.goto(x * 10, y * 10) #Scale up the cordinates for better visibility

def sample_points_along_heart():
    points = []
    for f in np.linspace(0, 2*np.pi, 5000):
        x = 16 * np.sin(f) ** 3
        y = 13 * np.cos(f) - 5 * np.cos(2 * f) - 2 * np.cos(3 * f) - np.cos(4 * f)
        points.append((x * 10, y * 10)) #Scale up the cordinates for better visibility
    return points # Return the sampled points

def fireworks():
    t = turtle.Turtle()
    s = turtle.Screen()


    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    t.speed(0)

    heart_points = sample_points_along_heart()

    if not heart_points:
        print("Error: No points sampled along the heart curve")


    for _ in range(50):

        # Randomly select a point on the heart curve

        x,y = random.choice(heart_points)

        t.penup()
        t.goto(x,y) # Go to the selected point
        t.pendown()

        color = random.choice(colors)
        t.color(color)

        #Draw particles for the firework burst

        for _ in range(5):
            t.penup()
            t.forward(random.randint(5, 30))
            t.right(random.randint(0, 360))
            t.pendown()
            t.dot(random.randint(2,5), color)


        #Clear the previous fireworks
        t.clear()

        #Write i love you s2
        t.penup()
        t.goto(0,0)
        t.pendown()
        t.write("I love you", align="center", font=("Arial", 30, "normal"))

if __name__ == "__main__":
    Desenhando()
    fireworks()
    turtle.done()
