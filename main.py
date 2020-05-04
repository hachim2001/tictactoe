
matt =[["0","0","0"],["0","0","0"],["0","0","0"]]
mat = matt
def show():
    print(mat[0],mat[1],mat[2],sep="\n")

def win(x,y,id):
    if mat[x-1][y] == id and mat[x-2][y] == id : return True
    if mat[x][y-1] == id and mat[x][y-2] == id : return True
    if mat[x-1][y-1] == id and mat[x-2][y-2] == id : return True
    return False

def chs(tkn, plr):
    x,y = 0, int(tkn[1])
    if tkn[0] == "b":
        x = 1
    elif tkn[0]== "c":
        x = 2
    elif tkn[0] == "a":
        x=0
    else:
        raise Exception("wrong coord")
    if mat[x][y] != "0" : 
        raise Exception("already chosen")
    mat[x][y] = plr

    show()
    return win(x,y,plr)
    



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
                continue
        else:
            try:
                if chs(cmd,pl):
                    print("the winner is ",pl)
                    game = False
                    mat = matt
                    continue

                pl = not pl
            except Exception as e:
                print(e)
            
