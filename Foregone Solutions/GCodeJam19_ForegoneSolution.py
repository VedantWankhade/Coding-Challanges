#----------------------------------------------------------------------------------------------------
''' 
PROBLEM
    Someone just won the Code Jam lottery, and we owe them N jamcoins! However, when we tried to print out
    an oversized check, we encountered a problem. The value of N, which is an integer, includes at least 
    one digit that is a 4... and the 4 key on the keyboard of our oversized check printer is broken.

    Fortunately, we have a workaround: we will send our winner two checks for positive integer amounts A 
    and B, such that neither A nor B contains any digit that is a 4, and A + B = N. Please help us find 
    any pair of values A and B that satisfy these conditions.

INPUT
    The first line of the input gives the number of test cases, T. T test cases follow; each consists of 
    one line with an integer N.

OUTPUT
    For each test case, output one line containing Case #x: A B, where x is the test case number (starting
    from 1), and A and B are positive integers as described above.

    It is guaranteed that at least one solution exists. If there are multiple solutions, you may output 
    any one of them.

SAMPLE
    Input       Output
        
    3           
    4           Case #1: 2 2
    940         Case #2: 852 88
    4444        Case #3: 667 3777
''' 
#----------------------------------------------------------------------------------------------------

def divide(n):                      # Function to divide the number into two numbers w/o 4
    n1 = list(str(n))               # Convert the number into list for easy access of each digit
    d1 = []                         # d1 and d1 
    d2 = []                         # to store the two aquired numbers
    for i in range(len(n1)):
        if int(n1[i]) == 4:         # If digit is 4 then substract 1 from it
            d1.append(1)            # else substract 0 from it
        else :
            d1.append(0)
        d2.append(int(n1[i]) - d1[i])

    return d1,d2                    # Return d1 and d2 as lists

tests=int(input())

for i in range(tests):
    n = int(input())  
    d1,d2 = divide(n)
    print('Case #%d:'%(i+1),end=' ')    # To print in format -- Case #1: 2 2 --
    print(int(''.join(map(str,d1))),end=' ')
    print(int(''.join(map(str,d2))))
#----------------------------------------------------------------------------------------------------