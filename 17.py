class Cell:
    def __init__(self,x,y,color='none'):
        self.color=color
        self.x=x
        self.y=y
        self.checked=False
        self.block= True
    def check(self):
        global mtrx
        self.checked = True
        if mtrx[self.x][self.y-1].color=='none' or mtrx[self.x][self.y+1].color=='none' or mtrx[self.x-1][self.y].color=='none' or mtrx[self.x+1][self.y].color=='none' :
            self.checked = True
            self.block = False
            return
        if mtrx[self.x][self.y-1].color==self.color :

            if mtrx[self.x][self.y-1].checked==False:
                mtrx[self.x][self.y-1].check()
            if mtrx[self.x][self.y-1].block==False:

                self.block = False
                self.checked = True
                return
        if mtrx[self.x][self.y+1].color==self.color :

            if mtrx[self.x][self.y+1].checked==False:
                mtrx[self.x][self.y+1].check()
            if mtrx[self.x][self.y+1].block==False:

                self.block = False
                self.checked = True
                return
        if mtrx[self.x-1][self.y].color==self.color :

            if mtrx[self.x-1][self.y].checked==False:
                mtrx[self.x-1][self.y].check()
            if mtrx[self.x-1][self.y].block==False:

                self.block = False
                self.checked = True
                return
        if mtrx[self.x+1][self.y].color==self.color :

            if mtrx[self.x+1][self.y].checked==False:
                mtrx[self.x+1][self.y].check()
            if mtrx[self.x+1][self.y].block==False:

                    self.block = False
                    self.checked = True
                    return
            self.checked = True
            self.block = True
mtrx=list()
def cretMap(a):
    global mtrx
    d=list()

    for i in range(a+2):
        for j in range(a+2):
            d.append(Cell(i,j))
        mtrx.append(d)
        d=[]
    for i in range(a+2):
        mtrx[0][i].color='wall'
        mtrx[i][0].color = 'wall'
        mtrx[i][a+1].color='wall'
        mtrx[a+1][i].color = 'wall'
a=int(input())
cretMap(a)
for i in range(a+2):
    for j in range(a+2):
        print(mtrx[i][j].color,end=' ')
    print()

