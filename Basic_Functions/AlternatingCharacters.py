def alternatingCharacters(s):
    if len(s) == 1:
        return int(0)
        print(s)
    for a in range(len(s)-1):
        if s[a] == s[a+1]:
            s.pop(a+1)
            print(s)
            return 1+alternatingCharacters(s)
        else:
            print(s)
            continue
    return 0

e = alternatingCharacters(list(input('input')))
print(e)

