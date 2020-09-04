def swap_case(s):
    j = ""
    for a in s:
        if a.islower():
            j = j + a.upper()
        elif a.isupper():
            j += a.lower()
        else:
            j += a
    return j


j = input(" Enter your string :")
print(swap_case(j))
