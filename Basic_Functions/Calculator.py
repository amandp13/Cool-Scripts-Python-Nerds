'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''


def calculate(**k):
    re = 0
    if k["operation"] == "add":
        re = k["first"] + k["second"]
    elif k["operation"] == "subtract":
        re = k["first"] - k["second"]
    elif k["operation"] == "multiply":
        re = k["first"] * k["second"]
    else:
        k["first"] / k["second"]
    if k["make_float"]:
        try :
            return k["message"] + " " + str(float(re))
        except :
            return "The result is" + " " +str(float(re))
    else:
        try :
            return k["message"] + " " + str(int(re))
        except :
            return "The result is" + " " +str(int(re))



print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))
