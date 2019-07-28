'''
GAME OF LIFE GUI SIMULATION 
ABHISHEK SRIVASTAVA
1MS17CS003
'''

import tkinter 
import turtle
import random
import sys

'''Class for representing the game grid and manipulating it'''
class GOL:
    '''
    Attributes:
    self.r->no of rows in grid
    self.c->no of columns in grid
    self.alive->set of tuples storing x and y coordinates of live cells
    Methods:
    __init__->constructor
    randomfill->fills grid randomly with life cells
    toggle->makes a live cell dead and a dead cell alive
    erase->removes all live cells from grid
    getAdj->counts the number of live neighbours to a given cell
    nextStep->generates next generation of cells
    draw->fills black color at a cell on the grid to make it alive
    printGrid->displays the grid
    '''
    
    def __init__(self,r,c):
        self.r=r
        self.c=c
        self.alive=set()
        
    def randomfill(self):
        self.erase()
        for i in range(0,self.r):
            for j in range(0,self.c):
                if random.random()>0.5:
                    self.alive.add((i,j))
                    
    def toggle(self,i,j):
        if (i,j) in self.alive:
            self.alive.remove((i,j))
        else:
            self.alive.add((i,j))
            
    def erase(self):
        self.alive=set()
        
    def getAdj(self,x,y):
        cnt=0
        for i in range(max(x-1,0),min(x+2,self.r)):
            for j in range(max(y-1,0),min(y+2,self.c)):
                if (i,j) in self.alive:
                    cnt+=1
        if (x,y) in self.alive:
            cnt-=1
        return cnt
        
    def nextStep(self):
        d=set()
        for i in range(self.r):
            for j in range(self.c):
                cnt=self.getAdj(i,j)

                if cnt==3:
                    d.add((i,j))
                elif cnt==2 and (i,j) in self.alive:
                    d.add((i,j))
                else:
                    pass
        self.alive=d

    def draw(self,x,y):
        global CELL_SIZE
        turtle.penup()
        if (x,y) in self.alive:
            turtle.setpos(x*CELL_SIZE,y*CELL_SIZE)
            turtle.color('black')
            turtle.pendown()
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(CELL_SIZE-1)
                turtle.left(90)
            turtle.end_fill()
            
    def printGrid(self):
        turtle.clear()
        for i in range(self.r):
            for j in range(self.c):
                self.draw(i,j)
        turtle.update()
    
def display_help_window():
    #create root window
    global root
    root=tkinter.Tk()
    root.geometry('380x500+0+100')
    root.title('Game of Life')

    #create widgets
    l=tkinter.Label(root,text="INSTRUCTIONS",bg='yellow',bd=5,font=('Consolas',14))
    l1=tkinter.Label(root,text="Click anywhere inside the grid to \nmake a cell alive or dead",bg='light blue',bd=5,font=('Consolas',14))
    l2=tkinter.Label(root,text="Press S to display \nnext generation of cells",bg='light green',bd=5,font=('Consolas',14))
    l3=tkinter.Label(root,text="Press C to continuously display \nsubsequent generation of cells",bg='light blue',bd=5,font=('Consolas',14))
    l4=tkinter.Label(root,text="Press E to erase the \ncurrent game grid",bg='light green',bd=5,font=('Consolas',14))
    l5=tkinter.Label(root,text="Press R to randomly \nfill the game grid",bg='light blue',bd=5,font=('Consolas',14))
    l6=tkinter.Label(root,text="Press Q to quit the game",bg='light green',bd=5,font=('Consolas',14))
    l7=tkinter.Label(root,text="HAPPY PLAYING!\nDISCOVER NEW PATTERNS!",bg='yellow',bd=5,font=('Consolas',14))

    #place widgets on the root window
    l.pack()
    l1.pack()
    l2.pack()
    l3.pack()
    l4.pack()
    l5.pack()
    l6.pack()
    l7.pack()


def main():
    global CELL_SIZE
    CELL_SIZE=int(input("Enter cell size in pixels:"))
    display_help_window()

    turtle.title("Game of life-grid")
    turtle.setworldcoordinates(0,0,400,300)

    turtle.hideturtle()
    turtle.speed('fastest')
    turtle.tracer(0,0)
    turtle.penup()

    board=GOL(400//CELL_SIZE,300//CELL_SIZE)

    #Mouse operations
    def toggle(x,y):
        i=x//CELL_SIZE
        j=y//CELL_SIZE
        board.toggle(i,j)
        board.printGrid()

    turtle.onscreenclick(toggle)

    #Keyboard operations
    def erase():
        board.erase()
        board.printGrid()
    def randomfill():
        board.randomfill()
        board.printGrid()

    continuous=True    
    def step():
        board.nextStep()
        board.printGrid()
        if continuous:
            turtle.ontimer(step,25)
    def stepOnce():
        nonlocal continuous
        continuous=False
        step()
    def stepContinuous():
        nonlocal continuous
        continuous=True
        step()

    def endprog():
        root.destroy()
        turtle.bye()
        sys.exit(1)


    turtle.onkey(erase,'e')
    turtle.onkey(randomfill,'r')
    turtle.onkey(stepOnce,'s')
    turtle.onkey(stepContinuous,'c')
    turtle.onkey(endprog,'q')
    turtle.listen()

    turtle.mainloop()
    root.mainloop()

main()
