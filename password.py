import random
import string

def strength(input_string): 
	
	n = len(input_string) 

	# Checking lower alphabet in string 
	hasLower = False
	hasUpper = False
	hasDigit = False
	specialChar = False
	normalChars = "abcdefghijklmnopqrstu"
	"vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
	
	for i in range(n): 
		if input_string[i].islower(): 
			hasLower = True
		if input_string[i].isupper(): 
			hasUpper = True
		if input_string[i].isdigit(): 
			hasDigit = True
		if input_string[i] not in normalChars: 
			specialChar = True

	# Strength of password 
	print("Strength of password:-", end = "") 
	if (hasLower and hasUpper and hasDigit and specialChar and n >= 8): 
		print("Strong") 
		
	elif (hasLower and hasUpper and hasDigit or specialChar and n > 6): 
		print("Moderate") 

	else: 
		print("Weak") 

input_string = input("Enter your password: ")
strength(input_string)

answer = input("Do you want me to create a password for you?\nPlease enter Yes or No: ").lower()
    
if answer == "yes":
        
    length = int(input("Enter the number of letters the password should have: "))
    password_characters = string.ascii_letters + string.digits      # + string.punctuation
    password = ''.join(random.choice(password_characters)  for i in range(length))
    print("Your Password will be: ", password)
    print("Thank You")
    
elif answer == "no":
    print("Thank You")
    
elif answer!= "yes" or "no":
    print("Invalid command.\nPlease try again.")
    
    
    
    
  





















