import sys
sys.stdin = open('2007input.txt','r')

T = int(input())
for tc in range(1,T+1):
    pattern = input()
    for i in range(1,10):
        if pattern[0:i]==pattern[i:2*i]:
            print('#{} {}'.format(tc,len(pattern[0:i])))
            break