#Given a random integer array A of size N. Find and print the count of pair of elements in the array which sum up to 0.
#Note: Array A can contain duplicate elements as well.

#Input format:
#The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol N.
#The following line contains N space separated integers, that denote the value of the elements of the array.
#Output format :
#The first and only line of output contains the count of pair of elements in the array which sum up to 0. 
#6
#0 0 0 0 -2 2
#o/p: 7

from sys import stdin


def pairSum0(arr, n):
    if n == 0:
        return 0
    s = {}
    count = 0
    for i in arr:
        s[i] = s.get(i, 0) + 1
        if s.get(-i, 0) and i:
            count = count + s[-i]
    if s.get(0, 0):
        zero = s[0] * (s[0] - 1)
        final = zero // 2
        count = count + final
    return count



def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(pairSum0(arr,n))
