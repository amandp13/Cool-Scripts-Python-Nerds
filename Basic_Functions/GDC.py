def mdc(a,b):
    resto = a%b
    if resto == 0:
        return b
    else:
        return mdc(b,resto)

x = int(input())
z = int(input())
print(mdc(x,z))
