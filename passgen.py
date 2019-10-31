#!/usr/bin/python
from random import Random

# Alphanumeric
num='1234567890'
lower='qwertyuiopasdfghjklzxcvbnm'
upper=lower.upper()
punc = "!@#$%^&*?"

# This function is what is called by GUI
def passgen(length=8, allow_num=True, allow_lower=True, allow_upper=True, allow_punc=False, blacklist="O10l"):


	# Configure what chars are to be used
	allchars=""
	if allow_num:
		allchars += num
	
	if allow_lower:
		allchars += lower
	
	if allow_upper:
		allchars += upper
	
	if allow_punc:
		allchars += punc
		
	# spits out an error if no characters are available for use
	if allchars == "":
		password = "No characters available to generate password!"
		return password
	
	for char in blacklist:
		allchars = allchars.replace(char,'')
	
	# Generate Password
	rng = Random()
	password = range(length)
	for i in password:
		password[i] = rng.choice(allchars)
	
	password = "".join(password)
	
	# Print password to screen for terminal use
	print password
	
	# Return password for gui
	return password
			

	
def main():		
	passgen()		

if __name__ == "__main__":
	main()
