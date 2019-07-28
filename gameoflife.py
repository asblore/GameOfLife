'''Game of Life Console Application
   ABHISHEK SRIVASTAVA
   1MS17CS003
'''

import random

'''Class to represent and manipulate game of life grid'''
class GOL:
    '''
       Attributes:
       self.r->an integer storing no of rows in grid
       self.c->an integer storing no of columns in grid
       self.lst->a 2D matrix storing the grid
       Methods:
       __init__->Constructor
       printGrid->prints the grid
       getAdj->counts number of live cells around a given cell
       nextStep->Creates next generation of cells
       placeLivingCellsRandomly->place live cells randomly
       isEmptyGrid->checks if grid has only dead cells or not
       setAlive->sets a cell alive
       still_life->generates stll life patterns
    '''
    def __init__(self,r,c):
        self.lst=[]
        self.r=r
        self.c=c 
        for i in range(r):
            l=[]
            for j in range(c):
                l+=['-']
            self.lst+=[l]

    def printGrid(self):
        for i in range(self.r):
            for j in range(self.c):
                print(self.lst[i][j],end=' ')
            print()
        print()

    def getAdj(self,x,y):
        cnt=0
        for i in range(max(0,x-1),min(x+2,self.r)):
            for j in range(max(0,y-1),min(y+2,self.c)):
                if self.lst[i][j]=='*':
                    cnt+=1

        if self.lst[x][y]=='*':
            cnt-=1

        return cnt

    def nextStep(self):
        ls=[]
        for i in range(self.r):
            l=[]
            for j in range(self.c):
                l+=['-']
            ls+=[l]
                
        for i in range(self.r):
            for j in range(self.c):
                cnt=self.getAdj(i,j)
                
                if cnt==3:
                    ls[i][j]='*'
                elif cnt==2 and self.lst[i][j]=='*':
                    ls[i][j]='*'
                else:
                    ls[i][j]='-'

        self.lst=ls
                    
    def placeLivingCellsRandomly(self,n):
        c=0
        while c<n:
            i=random.randrange(self.r)
            j=random.randrange(self.c)
            if self.lst[i][j]=='-':
                self.lst[i][j]='*'
                c+=1

    def isEmptyGrid(self):
        i=0
        while i<self.r:
            if self.lst[i].count('*')!=0:
                break
            i+=1

        if i==self.r:
            return True
        else:
            return False

    def setAlive(self,i,j):
        self.lst[i][j]='*'

    def still_life(self,n):
        if n<4:
            print("No still life patterns are possible with only "+str(n)+" live cells")
        else:
            print("Some of the still life patterns possible are:")
            if n==4:
                self.setAlive(2,2)
                self.setAlive(2,3)
                self.setAlive(3,2)
                self.setAlive(3,3)

                self.setAlive(5,5)
                self.setAlive(4,6)
                self.setAlive(5,7)
                self.setAlive(6,6)
            elif n==5:
                self.setAlive(3,3)
                self.setAlive(3,4)
                self.setAlive(4,3)
                self.setAlive(4,5)
                self.setAlive(5,4)
            elif n==6:
                self.setAlive(4,1)
                self.setAlive(3,2)
                self.setAlive(3,3)
                self.setAlive(4,4)
                self.setAlive(5,3)
                self.setAlive(5,2)

                self.setAlive(6,6)
                self.setAlive(6,7)
                self.setAlive(7,6)
                self.setAlive(7,8)
                self.setAlive(8,7)
                self.setAlive(8,8)
            elif n==7:
                self.setAlive(1,1)
                self.setAlive(1,2)
                self.setAlive(2,1)
                self.setAlive(2,3)
                self.setAlive(3,3)
                self.setAlive(4,3)
                self.setAlive(4,4)

                self.setAlive(5,7)
                self.setAlive(5,8)
                self.setAlive(6,6)
                self.setAlive(6,9)
                self.setAlive(7,7)
                self.setAlive(7,9)
                self.setAlive(8,8)
            elif n==8:
                self.setAlive(0,2)
                self.setAlive(0,3)
                self.setAlive(1,1)
                self.setAlive(1,4)
                self.setAlive(2,1)
                self.setAlive(2,4)
                self.setAlive(3,2)
                self.setAlive(3,3)

                self.setAlive(5,9)
                self.setAlive(5,8)
                self.setAlive(6,9)
                self.setAlive(7,8)
                self.setAlive(8,5)
                self.setAlive(8,7)
                self.setAlive(9,5)
                self.setAlive(9,6)
            elif n==9:
                self.setAlive(0,2)
                self.setAlive(1,1)
                self.setAlive(1,3)
                self.setAlive(2,1)
                self.setAlive(2,3)
                self.setAlive(3,0)
                self.setAlive(3,1)
                self.setAlive(3,3)
                self.setAlive(3,4)

                self.setAlive(5,9)
                self.setAlive(5,8)
                self.setAlive(6,9)
                self.setAlive(6,7)
                self.setAlive(7,7)
                self.setAlive(8,7)
                self.setAlive(8,5)
                self.setAlive(9,5)
                self.setAlive(9,6)
            else:
                self.setAlive(2,3)
                self.setAlive(2,4)
                self.setAlive(3,2)
                self.setAlive(3,5)
                self.setAlive(4,3)
                self.setAlive(4,5)
                self.setAlive(5,2)
                self.setAlive(5,3)
                self.setAlive(5,5)
                self.setAlive(5,6)
                
'''User defined exception to terminate program if Y/N is not input when needed'''
class YNError(Exception):
    pass

'''User defined exception which occurs if no of live cells exceeds grid capacity'''
class SizeError1(Exception):
    pass

'''User defined exception which occurs if no of live cells exceeds 10 for finding still life patterns'''
class SizeError2(Exception):
    pass


def main():
    try:
        print("WELCOME TO THE GAME OF LIFE")
    
        ch='N'
        while ch=='N':
            print("MENU")
            print("1.PLAY GAME WITH RANDOMLY GENERATED PATTERN")
            print("2.PLAY GAME WITH YOUR OWN PATTERN")
            print("3.FIND STILL LIFE PATTERNS IN GRID")
            choice=int(input("Enter your choice(1-3):"))

            if choice==1 or choice==2:
                r=int(input("Enter number of rows you want in the game grid:"))
                c=int(input("Enter number of columns you want in the game grid:"))
                grid=GOL(r,c)
                print("Your grid has been created. It is empty(has only dead cells).")
                print("A live cell is denoted by '*' and a dead cell is denoted by '-'.")
                grid.printGrid();
                n=r*c+1
                while n>r*c:
                    n=int(input("Enter the number of live cells you want in the grid:"))
                    if n>r*c:
                        print("Number of live cells exceeds grid capacity. Give input again.")
                
                if choice==1:
                    grid.placeLivingCellsRandomly(n);
                else:
                    i=0
                    while i<n:
                        x=int(input("Enter row index (0 to "+str(r-1)+") of cell you want to make alive:"))
                        if x>r-1:
                            print("Invalid row index. Enter again.")
                            continue
                        y=int(input("Enter column index (0 to "+str(c-1)+") of cell you want to make alive:"))
                        if y>c-1:
                            print("Invalid column index. Enter again.")
                            continue
                        grid.setAlive(x,y)
                        i+=1
                
                print("The grid is:")
                grid.printGrid()

                cho='Y'
                while not grid.isEmptyGrid():
                    cho=input("Want to view next generation grid?(Y/N):")
                    if cho!='Y' and cho!='N':
                        raise YNError
                    if cho=='N':
                        break
                    grid.nextStep()
                    print("The grid is:")
                    grid.printGrid()
            elif choice==3:
                n=11
                while n>10:
                     n=int(input("Enter the number of live cells you want in the grid(max 10):"))
                     if n>10:
                         print("The maximum input you can give is 10. Give input again.")
                grid=GOL(10,10)
                if n<4:
                    print("No still life patterns are possible with less than 4 live cells.")
                else:
                    print("Some of the still life patterns possible with",n,"live cells on the grid are:")
                    grid.still_life(n)
                    grid.printGrid()
                    print("The next generation of cells is:")
                    grid.nextStep()
                    grid.printGrid()
                    print("Thus the dead cells remain dead and live cells remain alive.")
            else:
                 print("Wrong choice!")
            ch=input("Do you want to quit?(Y/N):")
            if ch!='Y' and ch!='N':
                raise YNError
    except ValueError:
        print("Input must be an integer. Program terminated.")
    except YNError:
        print("Input must be Y or N. All other inputs are invalid. Program terminated.")

main()
