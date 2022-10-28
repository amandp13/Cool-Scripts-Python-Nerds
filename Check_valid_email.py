email=input("Enter Your E-mail: ");
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@"in email) and (email.count("@")==1): 
            if (email[-4]==".") ^ (email[-3]=="."): #since "." should be at -4 or at -3 at a time thats why XOR
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Wrong E-mail !!! Invalid Character Use")
            else:
                print("Wrong E-mail !!! . is not at right position")

        else:
            print("Wrong E-mail !!! Counting Of @ Should Be 1")
    else:
        print("Wrong Email !!! First Character Should be an Alphabet")
else:
    print("Wrong E-mail !!! Length Should Be Greater Or Equal to 6")
