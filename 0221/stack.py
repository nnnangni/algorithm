def find(s):
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        elif s[i] == ')':
            if len(stack) == 0:
                return -1 # 닫는 괄호가 남은 경우
            stack.pop()
        print(stack)
    if len(stack) != 0: # 여는 괄호가 남은 경우
        return -1
    else:
        return 1

T = int(input())
for tc in range(T):
    s = input()
    stack = []
    print(find(s))

# input
# 2
# ( )( )((( )))
# ((( )((((( )( )((( )( ))((( ))))))