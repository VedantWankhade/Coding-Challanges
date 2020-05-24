def findHill(list):
    hill_count = 0
    for i in range(1,len(list)-1):
        if list[i]>list[i-1] and list[i]>list[i+1]:
            hill_count += 1
    return hill_count

tests = int(input())
for j in range(tests):
    n = int(input())
    list = [int(x) for x in input().split()]
    hill_count = findHill(list)
    print('Case #{}: {}'.format(j+1,hill_count))