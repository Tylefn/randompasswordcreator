from random import randrange #Random number generator library
def listToString(passwd):    #List to string function that I've copied from stackoverflow xd
    str1 = ""   
    return (str1.join(passwd))

i = 0                        # Created for the loop
passwd = []                  # List of the characters that will turn into a string as your password 

charList = [*"""qwertyuopasdfghjklizxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/"""] # List of the usable characters
while (1):
    try:
        hmc = int(input("How many characters do you want in your password ?: "))
        print("\n")
    except ValueError:
        print("Only numbers pls...\n\n")
    else:
        if (hmc < 0):
            print("Please only valid numbers...\n\n")
        else: 
            while (i != hmc): # Loop for adding random characters in the password list
                i = i + 1
                rand = randrange(93) # Creates a random number
                passwd.append(charList[rand]) # Selects a random character in our charList 
            print(listToString(passwd),"\nis your password\n")
            exit(0)





