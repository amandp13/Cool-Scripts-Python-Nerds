#Importing statement required.
import random

#Declaring min lengt of password.
MIN_LENGTH = 8

#Declaring list for character for password.
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   

LOWERCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                     'z'] 
  
UPPERCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                     'Z'] 
  
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
           '*', '(', ')'] 

#This function will generate password and print it.
def password_generator(pwd_len=MIN_LENGTH):    # Setting default length as min length if no arguments are passed.

    all_list = DIGITS + LOWERCASE_CHARACTERS + UPPERCASE_CHARACTERS +SYMBOLS

    # Getting at least one different character
    one_digit = random.choice(DIGITS)
    one_lowercase = random.choice(LOWERCASE_CHARACTERS)
    one_uppercase = random.choice(UPPERCASE_CHARACTERS)
    one_symbol = random.choice(SYMBOLS)

    # Making base passowrd with each character
    Strong_password = one_digit + one_lowercase + one_symbol + one_uppercase 

    # Adding remaining character to password
    for _ in range(pwd_len-4):
        Strong_password = Strong_password + random.choice(all_list)

    
    # Shuffling password 
    random.shuffle(list(Strong_password))

     # Printing password
    print(Strong_password)

# Main function to call our generator function
if __name__ == "__main__":

    print("Enter the desired length of password or type 'Default' for minimum length:")
    pwd_len = input() # Taking Length input.
    
    if pwd_len != "default":
        password_generator(int(pwd_len))
    else:
        password_generator()