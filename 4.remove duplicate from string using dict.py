def uniqueChar(arr):
    if len(arr) == 0:
        return -1
    s = {}
    new = ''
    for i in arr:
        s[i] = s.get(i, 0) + 1
        if s[i] == 1:
            new = new + i

    return new






# Main 
s=input() 
print(uniqueChar(s))
