# Categorizing password as Strong or  
# Weak in Python using Regex  
  
  
import re 
  
  
# Function to categorize password 
def password(v): 
    v=input()
   
    # the password should not be a 
    # newline or space 
    if v == "\n" or v == " ": 
        return "Password cannot be a newline or space!"
   
    # the password length should be in 
    # between 6 and 10
    if 6<= len(v) <= 10: 
   
        # checks for occurrence of a character  
        # three or more times in a row 
        if re.search(r'(.)\1\1', v): 
            return "Weak Password: Same character repeats three or more times in a row"
   
        # checks for occurrence of same string  
        # pattern( minimum of two character length) 
        # repeating 
        if re.search(r'(..)(.*?)\1', v): 
            return "Weak password: Same string pattern repetition"
   
        else: 
            return "Strong Password!"
   
    else: 
        return "Password length must be 9-20 characters!"
  
# Main method 
def main(): 
   
    # Driver code 
    print(password("Qggf!@ghf3")) 
    print(password("Gggksforgeeks")) 
    print(password("aaabnil1gu")) 
    print(password("Aasd!feasn")) 
    print(password("772*hd897")) 
    print(password(" ")) 
   
   
# Driver Code 
if __name__ == '__main__': 
    main() 