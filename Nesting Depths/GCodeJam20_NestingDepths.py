def nest(s1):
    s2 = ''
    flag = 0
    stack = []
    for i in range(len(s1)):
        if flag :
            if int(s1[i]) == int(s1[i-1]):
                stack.append(s1[i])
            elif int(int(s1[i]) > int(s1[i-1])):
                for x in range(int(s1[i])-int(s1[i-1])):
                    stack.append('(')
                stack.append(s1[i])
            else :
                for y in range(int(s1[i-1])-int(s1[i])):
                    stack.append(')')
                stack.append(s1[i])
            if s1[i+1:] == '' :
                for z in range(int(s1[i])):
                    stack.append(')')
        else :
            for j in range(int(s1[i])):
               stack.append('(')
            stack.append(s1[i])
            if s1[i+1:] == '' :
                for z in range(int(s1[i])):
                    stack.append(')')
        flag = 1
    for i in stack:
        s2 = s2 + i
    return s2

tests = int(input())
for i in range(tests):
    string=input()
    s2=nest(string)
    print('Case #%d:'%(i+1),end=' ')
    print(s2)