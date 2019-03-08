import sys
sys.stdin = open('1983input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    grade = {'A+':N/10,'A0':N/10,'A-':N/10,'B+':N/10,'B0':N/10,
             'C+': N/10,'C0':N/10,'C-':N/10,'D0':N/10}
    student = {}
    for i in range(1,N+1):
        a,b,c = map(int, input().split())
        total = a*0.35+b*0.45+c*0.2
        student[i]=total

    sorted(student.items(), key=lambda x: x[1], reverse=True)
