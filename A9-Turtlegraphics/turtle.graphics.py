import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.speed(1)
angle = 30


def drawTree(t, lineLength):
    if lineLength > 0 :
        print("forward")
        t.forward(lineLength)
        print("forward - left 30")
        t.left(30)
        print("drawTree(", t, lineLength-10 , ")")
        drawTree(t, lineLength- 10)
        print("right (" , angle ,")" )
        t.right(angle)
        print("right 2 (" , angle, ")" )
        t.right(angle)
        print("drawTree 2 (" , lineLength -10 ,")") 
        drawTree(t, lineLength - 10)
        print("left (" , angle, ")") 
        t.left(angle)
        print("backward (" , lineLength,")") 
        t.backward(lineLength)
        
    print("drawTree End")

lineLength = 60
t.left(90)
drawTree(t, lineLength)
