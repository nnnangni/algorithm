import sys
sys.stdin = open('1265input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, P = map(int,input().split())
    candy = ((N//P+1)**(N%P))*((N//P)**(P-N%P))
    print('#{} {}'.format(tc,candy))