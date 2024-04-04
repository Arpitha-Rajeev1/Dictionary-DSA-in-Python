def printPairDiffK(arr, k):
    n = len(arr)
    if n == 0:
        return 0
    s = {}
    count = 0
    for i in arr:
        s[i] = s.get(i, 0) + 1
        if (s.get(i + k, 0) or s.get(i - k)) and k:
            if s.get(i + k, 0):
                pos = s[i + k]
            elif s.get(i - k, 0):
                pos = s[i - k]
            if s.get(i - k, 0) and s.get(i + k, 0):
                pos = s[i + k] + s[i - k]
            count = count + pos

    if not k:
        for i in s:
            temp = s[i]
            zero = temp * (temp - 1)
            final = zero // 2
            count = count + final
    return count


n = int(input())
lst = list(int(i) for i in input().strip().split(' '))
k = int(input())
print(printPairDiffK(lst, k))
