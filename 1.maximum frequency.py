from sys import stdin

n = int(input())
arr = list(int(x) for x in stdin.readline().strip().split())
d = {}
maximum = 0

for num in arr:
    d[num] = d.get(num, 0) + 1

for i in d:
    if d[i] > maximum:
        maximum = d[i]
        num = i

print(num)


# OR
from sys import stdin
def maxfreq(arr):
    if len(arr)==0:
        return -1
    s = {}
    maxOcc = -1
    for i in arr:
        s[i] = s.get(i, 0) + 1
        if maxOcc < s[i]:
            maxOcc = s[i]
 
    for n in arr:
        if s[n] == maxOcc:
            return n


def takeInput():
    n = int(stdin.readline().strip())
    if n < 0:
        return list(), -1
    if n == 0:
        return list(), 0
    arr = list(map(int,stdin.readline().strip().split( )))
    return arr, n


arr, n = takeInput()
if n >= 0:
    print(maxfreq(arr))
