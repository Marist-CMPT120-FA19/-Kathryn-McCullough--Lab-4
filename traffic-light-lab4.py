
#name: Kathryn McCullough
#email-address: kathryn.mccullough1@marist.edu
#project description: create a traffic light graphic using a rectangle as the body and three circles as the lights.


from graphics import *

def light():
    win = GraphWin('traffic_light',300,300)
    
    rect= Rectangle (Point(30,10), Point(90,150))
    rect.setOutline("black")
    rect.setWidth(4)
    rect.setFill("white")
    rect.draw(win)


    
    red=Circle(Point(60,35), 20)
    red.setFill("red")
    red.setOutline ("black")
    red.setWidth(3)
    red.draw(win)

    yellow=Circle(Point(60,80),20)
    yellow.setFill("yellow")
    yellow.setOutline ("black")
    yellow.setWidth(3)
    yellow.draw(win)

    green=Circle (Point(60,125), 20)
    green.setFill("green")
    green.setOutline ("black")
    green.setWidth(3)
    green.draw(win)
    

light()

   
    

    
