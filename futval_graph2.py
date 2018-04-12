from graphics import *

def main():
    #Introduction
    print("This program plots the growth of a 10- year investment.")

    #Get principal and interest rate '
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))

    #create a grpahics window with labels on the left edge
    win = GraphWin("investment Growth Chart", 640, 480)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1,0), '0.0K').draw(win)
    Text(Point(-1,2500), '2.5K').draw(win)
    Text(Point(-1,5000), '5.0K').draw(win)
    Text(Point(-1,7500), '7.5K').draw(win)
    Text(Point(-1,10000), '10.0K').draw(win)

    #Draw bar for initial principal
    bar = Rectangle(Point(0,0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    #Draw a bar fdor each subsequent years
    for year in range(1,11):
        principal = principal * (1+apr)
        bar = Rectangle(Point(year, 0), Point(year+1,principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit.")
    win.close()

main()
