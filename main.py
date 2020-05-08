default = "0"
matt =[["0","0","0"],["0","0","0"],["0","0","0"]]
mat = matt

    

def chs(tkn,tab, plr):
    x,y = 0, int(tkn[1])
    if tkn[0] == "b":
        x = 1
    elif tkn[0]== "c":
        x = 2
    elif tkn[0] == "a":
        x=0
    else:
        raise Exception("wrong coord")
    print(x,y)
    tab.chose((x,y),plr)
    return x,y


class tab:
    def __init__(self , tab = None):
        if tab :
            self.tab = tab
        else:
            self.tab = matt
        self.last = []
    
    def show(self):
        print(self.tab[0],self.tab[1],self.tab[2], sep = "\n")
    
    def empty(self):
        self.res = []
        for i in range(3):
            for j in range(3):
                if self.tab[i][j] == default:
                    self.res.append((i,j))
        return self.res
    
    def win(self, x, plr):
        x,y = x
        if self.tab[x-1][y] == plr and self.tab[x-2][y] == plr : 
            return True
        if self.tab[x][y-1] == plr and self.tab[x][y-2] == plr : 
            return True
        if (x,y) in [(0,0),(1,1),(2,2)]:
            if self.tab[x-1][y-1]==plr and self.tab[x-2][y-2] == plr: return True
        if (x,y) in [(0,2),(1,1),(2,0)]:
            if self.tab[(x+1)%3][y-1] == plr and self.tab[(x+2)%3][y-2] == plr: return True
        return False

    def chose(self, x,plr):
        x,y = x
        if self.tab[x][y] != default:
            raise Exception("already chosen")
        self.tab[x][y] = plr
        self.last.append((x,y))
    
    def dlt(self):
        x,y = self.last.pop(-1)
        self.tab[x][y] = default
    


class computer:
    """ a class responsible of the computer response to the game move
            it is using a minimax algorithm to determin the next move
     """
    def __init__(self , curr_tab, plr):
        self.tab = curr_tab
        self.fict_tab = curr_tab
        self.curr = self.tab.empty()
        self.plr = plr 
    
    def val(self, i , plr):
        if self.fict_tab.win(i,plr):
            return 1
        else :
            self.fict_tab.chose(i,plr=plr)
            possible = self.fict_tab.empty()
            res = []
            if possible:
                for j in possible:
                    res.append(self.val(j,not plr))
                self.fict_tab.dlt()
                if not plr:
                    mmm= max
                else:
                    mmm = min
                k = mmm(zip(possible,res),key=lambda x:x[1])[1]
                f=0
                for d in res :
                    if d == k:
                        f+=k
                return -f
            else:
                self.fict_tab.dlt()
                return 0

    def chose(self):
        self.choices = self.tab.empty()
        vals = []
        for i in self.choices:
            vals.append(self.val(i,self.plr))
        print(vals,self.choices)
        return max(zip(self.choices,vals),key=lambda x: x[1])[0]

        
            



if __name__ == '__main__':
    loop = True
    game = False
    pl = True
    while loop :
        cmd = input(">>")
        if cmd == "q":
            loop = False
            break
        if not game:
            if cmd == "p":
                game = True
                curr_tab = tab()
                cm = computer(curr_tab,False)
                curr_tab.show()
                continue
        else:
            try:
        
                i = chs(cmd,curr_tab,True)
                curr_tab.show()
                if curr_tab.win(i,True):
                    print("you won!")
                    game = False
                    del cm
                    continue
                else:
                    j=cm.chose()
                    curr_tab.chose(j,False)
                    curr_tab.show()

                    if curr_tab.win(j,False):
                        print("the computer wins")
                        game = False
                        del cm
                        continue
            except Exception as e:
                print(e)
            
