T = input()
R = 0
L = 0
for i in range(len(T)):
    if T[i]=="(" and T[i+4]==")":
        for j in range(len(T)):
            if j<i:
                if T[j]=="@":
                    R+=1
            else:
                if T[j]=="@":
                    L+=1
print(R,L)