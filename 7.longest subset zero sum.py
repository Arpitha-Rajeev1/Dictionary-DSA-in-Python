#Given an array consisting of positive and negative integers, find the length of the longest subarray whose sum is zero.
#Input Format:
#The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol N.
#The following line contains N space separated integers, that denote the value of the elements of the array.
#Output Format
#The first and only line of output contains length of the longest subarray whose sum is zero.

def subsetSum(arr):
    n = len(arr)
    if n == 0:
        return 0
    s = {}
    sum = 0
    maximum = 0
    for i in range(n):
        sum += arr[i]
        if s.get(sum, False) is False and sum != 0:
            s[sum] = i
        elif sum == 0:
            temp = i + 1
            if temp > maximum:
                maximum = temp
        else:
            temp = i - s[sum]
            if temp > maximum:
                maximum = temp
    return maximum


n = int(input())
lst = list(int(i) for i in input().strip().split(' '))
print(subsetSum(lst))

#Sample Input 1:
#10 
#95 -97 -387 -435 -5 -70 897 127 23 284
#Sample Output 1:
#5

#6
#1 2 3 4 -10 10
#Expected Output
#5
