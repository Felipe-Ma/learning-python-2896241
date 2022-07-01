
def is_palindrome(userString):
	#print("Checking if the input is a palindrome!")
	#print(userString)
	backwardsString = userString[::-1]
	#print(backwardsString)
	if backwardsString == userString:
		return True
	else:
		return False

run = True
while (run):
	#ask user for input
	userString = input("Enter the string to test for palindrome or 'exit':")

	#exit if user enters exit
	if(userString == "exit"):
		run = False
		break

	#convert string to lowercase
	userString = userString.lower()

	#remove punctuation
	newstr = ""
	for x in newstr:
		if x.isalnum:
			newstr += x


	palBool = is_palindrome(userString)
	if palBool:
		print("Palindrome!")
	else:
		print("Not Palindrome!")