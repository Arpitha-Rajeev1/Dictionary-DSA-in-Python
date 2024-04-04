from sys import stdin

def longestConsecutiveSubsequence(arr,n): 
    if n == 0:
        return 0
    s = {}
    for i in arr:
        s[i] = True

    increase = 0
    decrease = 0
    maxlength = 0
    start = arr[0]
    end = 0
    for i in arr:
        m = i + 1
        n = i - 1
        increase = 0
        decrease = 0
        if s[i]:
            while s.get(m, 0):
                increase += 1
                s[m] = False
                m = m + 1
            while s.get(n, 0):
                decrease += 1
                s[n] = False
                n = n - 1
            if increase > decrease and increase >= maxlength and arr.index(start) >= arr.index(i):
                start = i
                maxlength = increase
                end = m - 1
            if decrease > increase and decrease > maxlength:
                start = n + 1
                maxlength = decrease
                end = i
        s[i] = False

    if end:
        return [start, end]
    else:
        return [start]





def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

    
# Main 
arr,n=takeInput()
ans = longestConsecutiveSubsequence(arr,n) 
# This ans array contains two numbers, ie, start and end of longest sequence respectively
print(*ans)
