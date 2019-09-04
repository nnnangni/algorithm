def shoot(i,j):
    global direction, game, H, W
    direction = game[i][j]
    if direction == "<":
        dj = j
        print("<")
        if 0 <= dj - 1<W:
            dj -= 1
            if game[i][dj] == "." or game[i][dj] == "-":
                shoot(i,dj)
            elif game[i][dj]=="*":
                game[i][dj]="."
                shoot(i,dj)
            elif game[i][dj]=="#":
                pass
    if direction == ">":
        dj = j
        print(">")
        if 0 <= dj + 1<W:
            dj += 1
            if game[i][dj] == "." or game[i][dj] == "-":
                shoot(i,dj)
            elif game[i][dj]=="*":
                game[i][dj]="."
                shoot(i,dj)
            elif game[i][dj]=="#":
                pass
    if direction == "^":
        di = i
        print("^")
        if 0 <= di - 1<H:
            di -= 1
            if game[i][di] == "." or game[i][di] == "-":
                shoot(i,di)
            elif game[i][di]=="*":
                game[i][di]="."
                shoot(i,di)
            elif game[i][di]=="#":
                pass
    if direction == "v":
        di = i
        print("v")
        if 0 <= di + 1<H:
            di += 1
            if game[i][di] == "." or game[i][di] == "-":
                shoot(i,di)
            elif game[i][di]=="*":
                game[i][di]="."
                shoot(i,di)
            elif game[i][di]=="#":
                pass
    return game

T = int(input())
for tc in range(1,T+1):
    H, W = map(int,input().split())
    game = [list(input()) for i in range(H)]
    N = int(input())
    push = list(input())
    for p in push:
        for i in range(H):
            for j in range(W):
                if game[i][j]=="^" or game[i][j]=="v" or game[i][j]=="<" or game[i][j]==">":
                    if p=="U":
                        print(i,j,"U")
                        game[i][j]="^"
                        if 0<=i-1<W:
                            if game[i-1][j]==".":
                                game[i-1][j]="^"
                                game[i][j]="."
                    if p=="D":
                        print(i, j,"D")
                        game[i][j]="v"
                        if 0<=i+1<W:
                            if game[i+1][j]==".":
                                game[i+1][j] = "v"
                                game[i][j] = "."
                    if p=="L":
                        print(i, j,"L")
                        game[i][j]="<"
                        if 0<=j-1<H:
                            if game[i][j-1]==".":
                                game[i][j-1]="<"
                                game[i][j]="."
                    if p=="R":
                        print(i, j,"R")
                        game[i][j]=">"
                        if 0<=j+1<H:
                            if game[i][j+1]==".":
                                game[i][j+1]="<"
                                game[i][j]="."
                    if p=="S":
                        print(i, j,"S")
                        shoot(i,j)

    print(game)