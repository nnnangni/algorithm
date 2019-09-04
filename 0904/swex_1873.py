def shoot(direction,i,j):
    global game, H, W
    if direction == "<":
        dj = j
        if 0 <= dj - 1<W:
            dj -= 1
            if game[i][dj] == "." or game[i][dj] == "-":
                shoot(direction,i,dj)
            if game[i][dj]=="*":
                game[i][dj]="."
            if game[i][dj]=="#":
                pass
        if dj==0:
            return game
    if direction == ">":
        dj = j
        if 0 <= dj + 1<W:
            dj += 1
            if game[i][dj] == "." or game[i][dj] == "-":
                shoot(direction,i,dj)
            if game[i][dj]=="*":
                game[i][dj]="."
            if game[i][dj]=="#":
                pass
        if dj==W-1:
            return game
    if direction == "^":
        di = i
        if 0 <= di - 1<H:
            di -= 1
            if game[di][j] == "." or game[di][j] == "-":
                shoot(direction,di,j)
            if game[di][j]=="*":
                game[di][j]="."
            if game[di][j]=="#":
                pass
        if di==0:
            return game
    if direction == "v":
        di = i
        if 0 <= di + 1<H:
            di += 1
            if game[di][j] == "." or game[di][j] == "-":
                shoot(direction,di,j)
            if game[di][j]=="*":
                game[di][j]="."
            if game[di][j]=="#":
                pass
        if di==H-1:
            return game
    return game

T = int(input())
for tc in range(1,T+1):
    H, W = map(int,input().split())
    game = [list(input()) for i in range(H)]
    N = int(input())
    push = list(input())

    for p in push:
        for x in range(H):
            for y in range(W):
                if game[x][y] == "^" or game[x][y] == "v" or game[x][y] == "<" or game[x][y] == ">":
                    i = x
                    j = y
        if p=="U":
            game[i][j]="^"
            if 0<=i-1:
                if game[i-1][j]==".":
                    game[i-1][j]="^"
                    game[i][j]="."
        elif p=="D":
            game[i][j]="v"
            if 0<=i+1<H:
                if game[i+1][j]==".":
                    game[i+1][j] = "v"
                    game[i][j] = "."
        elif p=="L":
            game[i][j]="<"
            if 0<=j-1:
                if game[i][j-1]==".":
                    game[i][j-1]="<"
                    game[i][j]="."
        elif p=="R":
            game[i][j]=">"
            if j+1<W:
                if game[i][j+1]==".":
                    game[i][j+1]=">"
                    game[i][j]="."
        elif p=="S":
            direction = game[i][j]
            shoot(direction,i,j)

    print("#{}".format(tc),end=" ")
    for i in game:
        print("".join(i))
