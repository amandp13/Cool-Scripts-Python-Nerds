# python program to generate 
# an OTP from the squares of the 
# odd digits 
  
  
def OTP(number): 
      
    # Finding the length  
    # of the string 
    length = len(number) 
      
    # Declaring an empty string  
    # for storing otp 
    otp = '' 
      
    # Iterating from index 1  
    # with step as 2 
    for odd in range(1, length, 2): 
          
        # Concatenating the output 
        # to the string  
        otp+= str(int(number[odd])**2) 
          
    print(otp[0:4]) 
  
# Driver code 
number = input()
OTP(number) 